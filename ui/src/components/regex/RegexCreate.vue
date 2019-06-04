<template>
  <b-card header-tag="header">
    <b-form method="post" @submit.prevent="create_regex">
      <b-row>
        <b-col cols="10">
          <b-form-input type="text" v-model.lazy="regex_value" placeholder="Regular Expression" required></b-form-input>
        </b-col>
        <b-col cols="1">
          <b-form-input type="text" v-model.lazy="regex_score" placeholder="Score" required></b-form-input>
        </b-col>
        <b-col class="text-right">
          <b-button type="submit" variant="primary" required><font-awesome-icon icon="plus" /></b-button>
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
  name: 'RegexCreate',
  data () {
    return {
        search_filter: '',
        regex_score: 80,
        regex_value: '',
    }
  },
  
  methods: {
   create_regex () {
    this.$http.post('filters/regex', { value: this.regex_value, score: this.regex_score })
      .then(EventBus.$emit('refreshtable', this.search_filter)
      )
    }
  }
}
</script>