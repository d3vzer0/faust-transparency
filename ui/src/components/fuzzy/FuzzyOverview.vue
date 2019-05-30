<template>
  <b-card header-tag="header">
    <server-side type="fuzzy" :dataloc="data_loc" :countloc="count_loc" :limit="limit" :filter="search_filter" :output="output" :expectedfields="expected_fields" :target="target_url"></server-side>
  </b-card>
</template>

<script>
import ServerSide from '@/components/tables/ServerSide'

export default {
  name: 'FuzzyOverview',
  components: {
    ServerSide
  },
  data(){
    return {
      search_filter: '',
      target_url: 'filters/fuzzy',
      count_loc: 'count',
      data_loc: 'data',
      limit: 30,
      expected_fields: {
        value: 'value',
        id: '_id.$oid',
        _showDetails: false
      },
      output: {
        value: { label:'Fuzzy Keyword' },
        id: { label:'ID' },
        show_delete: { label:'Delete' }
      }
    }
  },
  methods: {
 
  },
};
</script>
