<template>
  <div class="fuzzy">
    <b-row class="fuzzycreate top-10">
      <b-col cols="12">
        <fuzzy-create></fuzzy-create>
      </b-col>
    </b-row>
    <b-row class="fuzzyoverview top-50">
      <b-col cols="12">
        <fuzzy-overview></fuzzy-overview>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import FuzzyCreate from '@/components/fuzzy/FuzzyCreate'
import FuzzyOverview from '@/components/fuzzy/FuzzyOverview'

export default {
  name: 'Fuzzy',
  components: {
    FuzzyCreate,
    FuzzyOverview
  }
}
</script>
