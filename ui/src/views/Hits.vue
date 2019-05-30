<template>
  <div class="hits">
    <b-row class="hitsfilter top-10">
      <b-col cols="12">
        <hits-filter></hits-filter>
      </b-col>
    </b-row>
    <b-row class="hitsoverview top-50">
      <b-col cols="12">
        <hits-overview></hits-overview>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import HitsFilter from '@/components/hits/HitsFilter'
import HitsOverview from '@/components/hits/HitsOverview'

export default {
  name: 'Hits',
  components: {
    HitsOverview,
    HitsFilter
  }
}
</script>
