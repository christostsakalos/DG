<template>
  <q-page class="q-pa-sm">
    <transition-group appear>
    <q-card class="bg-grey-8 animated backInDown">
          <div class="q-pa-md">



    <q-table
      title="Vehicles"
      class="theme_color text-white"
      :rows="vehicles"
      :columns="columns"
      row-key="id"
      :rows-per-page-options="[5,10,15, 30, 50]"
      :loading="loading"
      :filter="filter"
      @request="onRequest"
      binary-state-sort
      loading-label = 'Loading!!!'

    >


        <template v-slot:body-cell-action="props">
          <q-td :props="props">
            <div class="q-gutter-sm">
              <EditVehicle :id="props.key" @page-refresh="Edit" />
              <q-btn dense color="black" @click="del(props.key)" icon="delete"/>
            </div>
          </q-td>
        </template>

    <template v-slot:top-right>
      <AddVehicle /> <q-space/>
        <q-input color="white"   label-color="white" debounce="200" v-model="filter" label="Search">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
    </template>
    
    </q-table>
  </div>
    </q-card>
    </transition-group>
  </q-page>
</template>

<script lang="ts">
import { ref, onMounted, computed } from 'vue'
import {useStore} from 'vuex'
import {api} from '../boot/axios'
import EditVehicle from './EditVehicle.vue'
import AddVehicle from './AddVehicle.vue'

import { useQuasar } from 'quasar'
// Later need to get dynamic columns from the api
const columns = [
  {
    name: 'id',
    required: true,
    label: 'id',
    align: 'left',
    field: row => row.id,
    format: val => `${val}`,
    sortable: true
  },
  { name: 'make', label: 'E-mail', field: 'make', sortable:true },
  { name: 'model', label: 'First Name', field: 'model',},
  { name: 'vehicleregistrationnumber', align: 'center', label: 'Vehicle Number', field: 'vehicleregistrationnumber', },
  { name: 'fueltype', label: 'Fueltype', field: 'fueltype',  },
  { name: 'first_name', label: 'Owner', field: 'first_name',  },
  { name: 'action', label: 'Action', field: 'action', align: 'left', },
]
export default {
  components:{ EditVehicle, AddVehicle},
  setup () {
    const $q = useQuasar()
    const rows = ref([])
    const filter = ref('')
    const loading = ref(false)
    const vehicles = ref([])
    const pagination = ref({
      sortBy: 'id',
      descending: false,
      page: 1,
      rowsPerPage: 15,
      rowsNumber: 15,
      filter: '',
    })
  const store = useStore();
function Edit(props){
        const { page, sortBy, rowsPerPage } = pagination.value
        const filter = ''
// /  const vehicles = props.vehicles
$q.loading.show()
 loading.value = true
   api.get(`vehicles/?size=${rowsPerPage}&ordering=${sortBy}&search=${filter}&page=${page}`).then (res =>{
 vehicles.value = res.data.data
         pagination.value.sortBy = res.data.pagination.sortBy
        pagination.value.rowsNumber = res.data.pagination.rowsNumber
        pagination.value.page = res.data.pagination.page
        pagination.value.rowsPerPage = res.data.pagination.rowsPerPage
  }).catch(err => {
                        console.log(err);
                    }).then
      loading.value = false
      $q.loading.hide()
 
}
      // call from server
     function onRequest (props) {
      const { page, sortBy, rowsPerPage } = props.pagination
      const filter = props.filter
      $q.loading.show()
      loading.value = true
/*       api.get(superadmin/vehicles/?ordering=id&page=1&search=test@buyer.com) */
      api.get(`vehicles/?size=${rowsPerPage}&ordering=${sortBy}&search=${filter}&page=${page}`).then
      ( response  => {
        vehicles.value = response.data.data
        pagination.value.sortBy = response.data.pagination.sortBy
        pagination.value.rowsNumber = response.data.pagination.rowsNumber
        pagination.value.page = response.data.pagination.page
        pagination.value.rowsPerPage = response.data.pagination.rowsPerPage
        console.log(props)
   //     console.log(pagination.value)
      }).catch(err => {
                        console.log(err);
                    }).then
      $q.loading.hide()
      loading.value = false}
    onMounted(() =>
         {
      // get initial data from server (1st page)
      onRequest(
          {
        pagination: pagination.value,
        filter: '',
      })
    })
  // Delete vehicle function
    const del = (key) => {
            $q.dialog({
        title: 'Confirm',
        message: 'Would you like to delete the vehicle?',
        cancel: true,
        color: 'orange',
        persistent: true
      }).onOk(() =>{
         api.delete(`vehicles/${key}`);
        vehicles.value = vehicles.value.filter((vehicles)=> vehicles.id !== key)
      }).onCancel(() => {
        return
      })
    }
    return {
      persistent: ref(false),
      filter,
      loading,
      pagination,
      columns,
      rows,
      vehicles,
      onRequest,
      Edit,
      del,
    }
  }
}
</script>

<style lang="scss" scoped>
  .q-chip__content {
    display: block;
    text-align: center;
  }
  .theme_color {
    background-color: #343a40 !important
  }
</style>