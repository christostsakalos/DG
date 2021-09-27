<template>
  <q-page class="row items-center justify-evenly">
  <div class='row q-mb-md q-col-gutter-md'>
 <p class="text-h6">Incomplete Jobs</p> <Completechart />
  </div>
   <div class='row q-mb-md q-col-gutter-md'>
 <p class="text-h6">Unpaid Jobs</p>   <Paidchart />
   </div>
  </q-page>
</template>

<script lang="ts">
import Completechart from '../components/charts/Completechart.vue'
import Paidchart from '../components/charts/Paidchart.vue';
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'PageIndex',
  components: { Paidchart, Completechart },

});
</script>
