<template>
    <div class="page-customers">
        <div class="columns is-multiline">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">{{ $t("Dashboard") }}</router-link></li>
                <li><router-link to="/customers">{{ $t("Customers") }}</router-link></li>
            </ul>
        </nav>
            <div class="column is-12">
                <h1 class="title">{{ $t("Customer Manager") }}</h1>

                <router-link :to="{ name: 'AddCustomer' }" class="button is-success mt-4">{{ $t("Add customer") }}</router-link>
                <div class="field has-addons">
  <div class="control">
    <br>
        <input class="input" type="text" placeholder="Search a customer..." v-model="search_term" @keyup="getCustomer">
  </div>
  <div class="control">
    <br>
<!--     <button class="button is-success" v-on:click ="getCustomer">
      Search
    </button> -->
  </div>
</div>
            </div>

            <div
                class="column is-10">
              <div class="table-container">
                <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                    <thead>
                    <tr class="th">
                        <th >{{ $t("Reference Number") }}</th>
                        <th>{{ $t("First Name") }}</th>
                        <th>{{ $t("Last Name") }}</th>
                        <th>{{ $t("Email") }}</th>
                        <th>{{ $t("Address") }}</th>
                        <th>{{ $t("City") }}</th>
                        <th>{{ $t("Country") }}</th>
                        <th>{{ $t("Action") }}</th>
                    </tr></thead>
                    
                    <tbody v-if="search_term.length <= 3" @keyup="load">
                   
                    <tr v-for="customer in customers" v-bind:key="customer.id" >
                        <td class="table is-narrow">{{ customer.reference_number }}</td>
                        <td class="table is-narrow">{{ customer.first_name }}</td>
                        <td class="table is-narrow">{{ customer.last_name }}</td>
                        <td class="table is-narrow">{{ customer.email }}</td>
                        <td class="table is-narrow">{{ customer.address }}</td>
                        <td class="table is-narrow">{{ customer.city }}</td>
                        <td class="table is-narrow">{{ customer.country }}</td>
                        <td class="table is-narrow"><router-link :to="{ name: 'Customer', params: { id: customer.id }}" class="button is-info">{{ $t("View") }}</router-link>
                        <router-link :to="{ name: 'CustomerEdit', params: { id: customer.id }}" class="button is-link">{{ $t("Edit") }}</router-link>
                        <button class="button is-danger" @click="Deletecustomer(customer.id)">{{ $t("Delete") }}</button></td>
                    </tr>
                 <Paginator :last-page="lastPage"  @page-changed="load($event)"/>   </tbody>
                    <tbody v-else-if="search_term.length >= 3">
                                          <tr v-for="customer in searched_customers" v-bind:key="customer.id">
                        <td class="table is-narrow">{{ customer.reference_number }}</td>
                        <td class="table is-narrow">{{ customer.first_name }}</td>
                        <td class="table is-narrow">{{ customer.last_name }}</td>
                        <td class="table is-narrow">{{ customer.email }}</td>
                        <td class="table is-narrow">{{ customer.address }}</td>
                        <td class="table is-narrow">{{ customer.city }}</td>
                        <td class="table is-narrow">{{ customer.country }}</td>
                        <td class="table is-narrow"><router-link :to="{ name: 'Customer', params: { id: customer.id }}" class="button is-info">{{ $t("View") }}</router-link>
                        <router-link :to="{ name: 'CustomerEdit', params: { id: customer.id }}" class="button is-link">{{ $t("Edit") }}</router-link>
                        <button class="button is-danger" @click="Deletecustomer(customer.id)">{{ $t("Delete") }}</button></td>
                    </tr>
               <PaginatorSearch :last-page="lastPagesearch" @page-changedsearch="getCustomer($event)" />
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
    name: 'Customers',
    components: {Paginator, PaginatorSearch},
  setup() {



    const customers = ref([]);
    const searched_customers = ref([]);
    const search_term = ref("");
    const lastPage = ref(0);
    const pagesearch = 1
    const lastPagesearch = ref(0);
    const search_results = ref([]);
    const load = async (page = 1) => {
      const response = await axios.get(`api/v1/customers/?page=${page}`);
      customers.value = response.data.data;
      lastPage.value = response.data.meta.last_page;}
    const getCustomer = async () => {
      const responsesearch = await axios.get(`api/v1/customers/?page=${pagesearch}&search=${search_term.value}`);
      searched_customers.value = responsesearch.data.data;
      lastPagesearch.value = responsesearch.data.meta.last_page;}

    onMounted(load);

    async function Deletecustomer (id = customer.id) {
      if (confirm('Are you sure you want to delete this record?')) {
           await axios.delete(`/api/v1/customers/${id}`);
            customers.value = customers.value.filter((customers)=> customers.id !== id)
            toast({
                        message: 'The customer has been removed',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })    
                     }
               
                  }
       
    return {
      customers,
      search_results,
      lastPage,
      lastPagesearch,
      load,
      getCustomer,
      search_term,
      searched_customers,
      pagesearch,
      Deletecustomer,

    
      
    }
  }
}
/* To do 1 : Add search functionality --- Done
To do 2 : Rework the delete function --- Done
To do 3 : Add the dbvehicle relationship --- Done
To do 4: Swap to mysql --- Done
To do 5: Improve pagination
To do 6: Improve the ui 
To do 7: fix the validators */
</script>

<style lang="scss" scoped>
</style>