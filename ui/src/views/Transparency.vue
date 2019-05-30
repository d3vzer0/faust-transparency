<template>
  <div class="transparency">
    <b-row class="transparencyfilter top-10">
      <b-col cols="12">
        <transparency-filter></transparency-filter>
      </b-col>
    </b-row>
    <b-row class="transparencyoverview top-50">
      <b-col cols="12">
      </b-col>
    </b-row>
  </div>
</template>

<script>
import TransparencyFilter from '@/components/transparency/TransparencyFilter'

export default {
  name: 'Transparency',
  components: {
    TransparencyFilter,
  }
}
</script>
