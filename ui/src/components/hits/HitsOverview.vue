<template>
  <b-card header-tag="header">
    <server-side type="hits" :dataloc="data_loc" :countloc="count_loc" :limit="limit" :filter="search_filter" :output="output" :expectedfields="expected_fields" :target="target_url"></server-side>
  </b-card>
</template>

<script>
import EventBus from '@/eventbus'
import ServerSide from '@/components/tables/ServerSide'

export default {
  name: 'HitsOverview',
  components: {
    ServerSide
  },
  data(){
    return {
      search_filter: '',
      count_loc: 'count',
      data_loc: 'results',
      target_url: 'hits',
      limit: 30,
      expected_fields: {
        timestamp: 'timestamp.$date',
        domain: 'domain',
        pattern_match: 'pattern_match',
        source: 'source',
        id: '_id.$oid',
        _showDetails: false
      },
      output: {
        timestamp: { label: 'Timestamp' },
        domain: { label:'Domain' },
        pattern_match: { label:'Pattern' },
        source: { label:'Source' },
      }

    }
  }
}
</script>
