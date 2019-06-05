<template>
  <b-card>
    <b-form method="get" @submit.prevent="filter_hits">
      <b-row>
        <b-col xl="11" md="10" cols="12">
          <b-form-input type="text" v-model="search_filter" placeholder="Domain"></b-form-input>
        </b-col>
        <b-col>
          <b-button type="submit" variant="primary" class="fullwidth"><font-awesome-icon icon="search" /></b-button>
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
  name: 'HitsFilter',
  data(){
    return {
    }
  },
  computed: {
    search_filter: {
      get () {
        return this.$store.getters['target/domain']
      },
      set (value) {
        this.$store.commit('target/update_domain', value)
      }
    }
  },
  methods: {
    filter_hits () {
      console.log(1)
      EventBus.$emit('refreshscreenshots', this.search_filter)
    }
  } 
}
</script>
