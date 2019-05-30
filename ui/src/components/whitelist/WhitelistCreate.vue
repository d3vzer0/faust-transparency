<template>
  <b-card header-tag="header">
    <b-form method="get" @submit.prevent="create_whitelist()">
      <b-row>
         <b-col cols="11">
          <b-form-input type="text" v-model="whitelist_domain" placeholder="Domain" required></b-form-input>
        </b-col>
         <b-col class="text-right">
          <b-button type="submit" variant="primary" class="fullwidth"><font-awesome-icon icon="plus" /></b-button>
        </b-col>
      </b-row>
    </b-form>
  </b-card>
</template>

<script>
import Vue from 'vue'
import EventBus from '@/eventbus'
Vue.use(require('vue-moment'))

export default {
  name: 'WhitelistCreate',
  data(){
    return {
        whitelist_domain: '',
        search_filter: ''
    }
  },
  methods: {
    create_whitelist () {
      // console.log(1)
      this.$http.post('whitelist', { value: this.whitelist_domain })
        .then(EventBus.$emit('refreshtable', this.search_filter)
      )
    }
  }
}

</script>