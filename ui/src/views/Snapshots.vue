<template>
  <div class="snapshots">
    <b-row class="snapshotsfilter top-10">
      <b-col cols="12">
        <snapshots-filter></snapshots-filter>
      </b-col>
    </b-row>
    <b-row class="snapshotsoverview top-10">
      <b-col cols="12">
        <snapshots-overview></snapshots-overview>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import SnapshotsFilter from '@/components/snapshots/SnapshotFilter'
import SnapshotsOverview from '@/components/snapshots/SnapshotOverview'

export default {
  name: 'Snapshots',
  components: {
    SnapshotsFilter,
    SnapshotsOverview
  }
}
</script>
