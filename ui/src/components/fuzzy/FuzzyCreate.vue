<template>
  <b-card>
    <b-form method="get" @submit.prevent="create_fuzzy">
      <b-row>
        <b-col cols="9">
          <b-form-input type="text" v-model.lazy="fuzzy_value" placeholder="Fuzzy String" required></b-form-input>
        </b-col>
         <b-col cols="1">
          <b-form-input type="text" v-model.lazy="fuzzy_likelihood" placeholder="%" required></b-form-input>
        </b-col>
        <b-col cols="1">
          <b-form-input type="text" v-model.lazy="fuzzy_score" placeholder="Score" required></b-form-input>
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
  name: 'FuzzyCreate',
  data(){
    return {
      search_filter: '',
      fuzzy_likelihood: 80,
      fuzzy_score: 80,
      fuzzy_value: '',
    }
  },
  methods: {
   create_fuzzy(){
     this.$http.post('filters/fuzzy', { value: this.fuzzy_value, score: this.fuzzy_score, likelihood: this.fuzzy_likelihood })
      .then(EventBus.$emit('refreshtable', this.search_filter)) 
   }
  },
  mounted (){
  }
  
};
</script>
