<template>
  <div class="whitelist">
    <b-row class="whitelistcreate top-10">
      <b-col cols="12">
        <whitelist-create></whitelist-create>
      </b-col>
    </b-row>
    <b-row class="hitsoverview top-50">
      <b-col cols="12">
        <whitelist-overview></whitelist-overview>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import WhitelistCreate from '@/components/whitelist/WhitelistCreate'
import WhitelistOverview from '@/components/whitelist/WhitelistOverview'

export default {
  name: 'Whitelist',
  components: {
    WhitelistCreate,
    WhitelistOverview
  }
}
</script>
