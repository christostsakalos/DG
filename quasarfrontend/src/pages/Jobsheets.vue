<template>
  <q-page class="q-pa-sm">
    <transition-group appear>
    <q-card class="bg-grey-8 animated backInDown">
          <div class="q-pa-md">



    <q-table
      title="Jobsheets"
      class="theme_color text-white"
      :rows="jobsheets"
      :columns="columns"
      row-key="id"
      v-model:pagination="pagination"
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
             
              <q-btn dense color="black" @click="del(props.key)" icon="delete"/>
            </div>
          </q-td>
        </template>

    <template v-slot:top-right>
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
  { name: 'reference_number', label: 'Reference', field: 'reference_number', sortable:true },
  { name: 'first_name', label: 'First Name', field: 'first_name',},
  { name: 'last_name', align: 'center', label: 'Last Name', field: 'last_name', },
  { name: 'email', label: 'Email', field: 'email',  },
  { name: 'status', label: 'Status', field: 'status', align: 'left', },
]
export default {
  components:{},
  setup () {
    const $q = useQuasar()
    const rows = ref([])
    const filter = ref('')
    const loading = ref(false)
    const jobsheets = ref([])
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
// /  const jobsheets = props.jobsheets
$q.loading.show()
 loading.value = true
   api.get(`jobsheets/?size=${rowsPerPage}&ordering=${sortBy}&search=${filter}&page=${page}`).then (res =>{
 jobsheets.value = res.data.data
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
/*       api.get(superadmin/jobsheets/?ordering=id&page=1&search=test@buyer.com) */
      api.get(`jobsheets/?size=${rowsPerPage}&ordering=${sortBy}&search=${filter}&page=${page}`).then
      ( response  => {
        jobsheets.value = response.data.data
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
  // Delete customer function
    const del = (key) => {
            $q.dialog({
        title: 'Confirm',
        message: 'Would you like to delete the customer?',
        cancel: true,
        color: 'orange',
        persistent: true
      }).onOk(() =>{
         api.delete(`jobsheets/${key}`);
        jobsheets.value = jobsheets.value.filter((jobsheets)=> jobsheets.id !== key)
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
      jobsheets,
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