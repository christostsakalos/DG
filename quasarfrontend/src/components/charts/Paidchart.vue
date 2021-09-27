<template>
<div id="wrapper">
<div class="columns">
 <MonthlyChart  v-bind:chartData="chartdata"  />
</div>

</div>
</template>

<script>
import {api} from '../../boot/axios'
import { defineComponent, onMounted, ref, onBeforeMount } from 'vue'
import MonthlyChart from './chart'

export default defineComponent({
  name: 'Paidchart',
  components: {
    MonthlyChart
  },

setup(){
    const dataCollection = ref([]);
    const chartdata = ref({});
        function load() {api.get(`paidchart`).then (response=>{
            dataCollection.value = response.data.data;
            chartdata.value = Object.assign({}, dataCollection.value)
            chartdata.value = chartdata.value[0]
          })}
onBeforeMount(load)
onMounted(load)

    return{
        load,
        dataCollection,
        chartdata,
    }

}


})
</script>