<template>
  <div class="regex">
    <b-row class="regexcreate top-10">
      <b-col cols="12">
        <regex-create></regex-create>
      </b-col>
    </b-row>
    <b-row class="regexoverview top-50">
      <b-col cols="12">
        <regex-overview></regex-overview>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import RegexCreate from '@/components/regex/RegexCreate'
import RegexOverview from '@/components/regex/RegexOverview'

export default {
  name: 'Regex',
  components: {
    RegexCreate,
    RegexOverview
  }
}
</script>
