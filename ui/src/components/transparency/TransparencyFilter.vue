<template>
  <b-card>
    <b-form method="get" @submit.prevent="filter_transparency">
      <b-row>
        <b-col cols="11">
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

export default {
  name: 'TransparencyFilter',
  data () {
    return {
    }
  },
  methods: {
   filter_transparency () {
    console.log(1)
    //  EventBus.$emit('refresh_transparency', this.$store.getters['target/domain'])
   }
  },
  computed: {
     search_filter: {
      get () {
        return this.$store.getters['target/domain'];
      },
      set (value) {
        this.$store.commit('target/update_domain', value);
      }
    }
  }
};
</script>