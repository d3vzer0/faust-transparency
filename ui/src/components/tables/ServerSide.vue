<template>
    <div class="serverside-table">
    <b-table striped ref="detailstable" fixed hover :fields="output" :items="search_results" :current-page="current_page" :per-page="limit">
      <template slot="show_details" slot-scope="row">
          <b-button size="sm" @click.stop="row.toggleDetails" variant="primary" class="mr-2">
            {{ row.detailsShowing ? 'Hide' : 'Show'}} Details
          </b-button>
      </template>
  
      <template slot="show_delete" slot-scope="row">
        <b-button size="sm" variant="primary" class="mr-2" v-on:click="delete_filter(row.item)">Delete</b-button>
      </template>

      <template slot="row-details" slot-scope="row">
      <b-card v-if="row.item.datasource == 'transparency'">
        <b-row >
          <b-col><b>Fingerprint</b></b-col>
          <b-col>{{row.item.details.fingerprint}}</b-col>
        </b-row>
        <b-row>
          <b-col><b>Issuer</b></b-col>
          <b-col>{{row.item.details.issuer.CN}}</b-col>
        </b-row>
        <b-row>
          <b-col><b>Not Before / Not After</b></b-col>
          <b-col>{{from_unix(row.item.details.not_before.replace('Z',''))}} / {{ from_unix(row.item.details.not_after.replace('Z',''))}}</b-col>
        </b-row>
      </b-card>
    </template>
    </b-table>
    <b-row>
      <b-col md="6">
        <b-pagination :total-rows="search_count" :per-page="limit" v-model="current_page" @change="get_results_filtered"/>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import _ from 'lodash'
import EventBus from '@/eventbus'

export default {
  name: 'GenericTable',
  props: ['type', 'filter', 'output', 'expectedfields', 'limit', 'target', 'countloc', 'dataloc', 'details'],
  data(){
    return {
      search_filter: this.$store.getters['target/domain'],
      search_results: [],
      search_count: 0,
      current_page: 1,
    }
  },
  beforeDestroy () {
    EventBus.$off('refreshtable', this.search_filter)
  },
  mounted () {
    EventBus.$on('refreshtable', search_filter =>{
        this.search_filter = search_filter
        this.get_results_filtered()
      })
    this.get_results_filtered()
  },
  methods: {
    get_results_filtered (page) {
      this.search_results = []
      const current_page = page ? page : this.current_page
      var skip_results = (current_page * this.limit) - this.limit;
      var query_params = {
        skip: skip_results, 
        limit: this.limit
      }
      if (this.search_filter != '') {
        query_params.search= this.search_filter
      }
      this.$http
        .get(this.target, { params:query_params })
        .then(response => this.parse_results_filtered(response))
        .catch()
    },
    parse_results_filtered (response) {
      var data = response.data;
      let items = _.get(data, this.dataloc)
      this.search_count = _.get(data, this.countloc)
      items.forEach(detail => {
        var field_mapping = {}
        for (const [key, value] of Object.entries(this.expectedfields)) {
          if (key == "timestamp") {
            _.set(detail, value, this.from_unix(_.get(detail, value)))
          }
          field_mapping[key] = _.get(detail, value)
        }
        this.search_results.push(field_mapping)
      });
    },
    delete_filter (item) {
      if (this.type === 'whitelist') {
        var url_path = `whitelist/${item.domain}`
      }
      else if (this.type === 'regex') {
        var url_path = `filter/regex/${item.regex}`
      }
      else if (this.type === 'fuzzy') {
        var url_path = `filter/fuzzy/${item.value}`
      }
      this.$http.delete(url_path)
        .then(response => this.get_results_filtered())
    },
    from_unix (unix_timestamp) {
      var from_miliseconds = Math.floor(unix_timestamp / 1000)
      var datetime = this.$moment.unix(from_miliseconds).format('YYYY-MM-DD HH:mm:ss')
      return datetime
    }
  }
};
</script>
