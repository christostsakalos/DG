<template>
    <div class="page-jobsheets">
        <div class="columns is-multiline">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">{{ $t("Dashboard") }}</router-link></li>
                <li><router-link to="/jobsheets">{{ $t("Jobsheets") }}</router-link></li>
            </ul>
        </nav>
            <div class="column is-12">
                <h1 class="title">{{ $t("Jobs Manager") }}</h1>

                <router-link :to="{ name: 'AddJobsheet' }" class="button is-success mt-4">{{ $t("Add jobsheet") }}</router-link>
                <div class="field has-addons">
  <div class="control">
    <br>
        <input class="input" type="text" placeholder="Search a jobsheet..." v-model="search_term" @keyup="getjobsheet">
  </div>
  <div class="control">
    <br>
  </div>
</div>
            </div>

            <div
                class="column is-13">
              <div class="table-container">
                <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                    <thead>
                    <tr class="th">
                        <th >{{ $t("Reference Number") }}</th>
                        <th>{{ $t("First Name") }}</th>
                        <th>{{ $t("Last Name") }}</th>
                        <th>{{ $t("Email") }}</th>
                        <th>{{ $t("Vehicleregistrationnumber") }}</th>
                        <th>{{ $t("Date Due") }}</th>
                        <th>{{ $t("Status") }}</th>
                        <th>{{ $t("Action") }}</th>
                    </tr></thead>
                    
                    <tbody v-if="search_term.length <= 3" @keyup="load">
                   
                    <tr v-for="jobsheet in jobsheets" v-bind:key="jobsheet.id" >
                        <td class="table is-narrow">{{ jobsheet.reference_number }}</td>
                        <td class="table is-narrow">{{ jobsheet.first_name }}</td>
                        <td class="table is-narrow">{{ jobsheet.last_name }}</td>
                        <td class="table is-narrow">{{ jobsheet.email }}</td>
                        <td class="table is-narrow">{{ jobsheet.vehicleregistrationnumber}}</td>
                        <td class="table is-narrow">{{ jobsheet.datedue }}</td>
                        <td class="table is-narrow">{{ jobsheet.status }}</td>
                        <td class="table is-narrow"><router-link :to="{ name: 'Jobsheet', params: { id: jobsheet.id }}" class="button is-info">{{ $t("View") }}</router-link>
                        <router-link :to="{ name: 'JobsheetEdit', params: { id: jobsheet.id }}" class="button is-link">{{ $t("Edit") }}</router-link>
                        <button class="button is-danger" @click="Deletejobsheet(jobsheet.id)">{{ $t("Delete") }}</button></td>
                    </tr>
                 <Paginator :last-page="lastPage"  @page-changed="load($event)"/>   </tbody>
                    <tbody v-else-if="search_term.length >= 3" >
                                          <tr v-for="jobsheet in searched_jobsheets" v-bind:key="jobsheet.id">
                        <td class="table is-narrow">{{ jobsheet.reference_number }}</td>
                        <td class="table is-narrow">{{ jobsheet.first_name }}</td>
                        <td class="table is-narrow">{{ jobsheet.last_name }}</td>
                        <td class="table is-narrow">{{ jobsheet.email }}</td>
                        <td class="table is-narrow">{{ jobsheet.vehicleregistrationnumber}}</td>
                        <td class="table is-narrow">{{ jobsheet.datedue }}</td>
                        <td class="table is-narrow">{{ jobsheet.status }}</td>

                        <td class="table is-narrow"><router-link :to="{ name: 'Jobsheet', params: { id: jobsheet.id }}" class="button is-info">{{ $t("View") }}</router-link>
                        <router-link :to="{ name: 'JobsheetEdit', params: { id: jobsheet.id }}" class="button is-link">{{ $t("Edit") }}</router-link>
                        <button class="button is-danger" @click="Deletejobsheet(jobsheet.id)">{{ $t("Delete") }}</button></td>
                    </tr>
               <PaginatorSearch :last-page="lastPagesearch" @page-changedsearch="getjobsheet($event)" />
               </tbody>
                </table>
              </div>

                      
            </div>
            </div>
    </div>
</template>

<script>
import {ref, onMounted, useRouter} from 'vue';
import { toast } from 'bulma-toast';
import axios from 'axios'
import Paginator from '@/components/paginators/Paginator'
import PaginatorSearch from '@/components/paginators/PaginatorSearch'
export default {
    name: 'Jobsheets',
    components: {Paginator, PaginatorSearch},
  setup() {



    const jobsheets = ref([]);
    const searched_jobsheets = ref([]);
    const search_term = ref("");
    const lastPage = ref(0);
    const pagesearch = 1;
    const lastPagesearch = ref(0);
    const search_results = ref([]);
    const load = async (page = 1) => {
      const response = await axios.get(`api/v1/jobsheets/?page=${page}`);
      jobsheets.value = response.data.data;
      lastPage.value = response.data.meta.last_page;
      }
      const getjobsheet = async () => {
      const responsesearch = await axios.get(`api/v1/jobsheets/?page=${pagesearch}&search=${search_term.value}`);
      searched_jobsheets.value = responsesearch.data.data;
      lastPagesearch.value = responsesearch.data.meta.last_page;}
    


    onMounted(load);

    async function Deletejobsheet (id = jobsheet.id) {
      if (confirm('Are you sure you want to delete this record?')) {
           await axios.delete(`/api/v1/jobsheets/${id}`);
            jobsheets.value = jobsheets.value.filter((jobsheets)=> jobsheets.id !== id)
            toast({
                        message: 'The jobsheet has been removed',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })    
                     }
               
                  }
       
    return {
      jobsheets,
      search_results,
      lastPage,
      pagesearch,
      lastPagesearch,
      load,
      getjobsheet,
      search_term,
      searched_jobsheets,
      Deletejobsheet,

    
      
    }
  }
}
</script>

<style lang="scss" scoped>
</style>