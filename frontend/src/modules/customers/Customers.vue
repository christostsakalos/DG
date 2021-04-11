<template>
    <div class="page-customers">
        <div class="columns is-multiline">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/customers">Customers</router-link></li>
            </ul>
        </nav>
            <div class="column is-12">
                <h1 class="title">Customer Manager</h1>

                <router-link :to="{ name: 'AddCustomer' }" class="button is-success mt-4">Add customer</router-link>
            </div>

            <div
                class="column is-8">
              <div class="table-container">
                <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                    <thead>
                    <tr class="th">
                        <th >Reference Number</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Address</th>
                        <th>City</th>
                        <th>Country</th>
                        <th>Action</th>
                    </tr></thead>
                    
                    <tbody v-for="customer in customers" v-bind:key="customer.id">
                   
                    <tr>
                        <td class="table is-narrow">{{ customer.reference_number }}</td>
                        <td class="table is-narrow">{{ customer.first_name }}</td>
                        <td class="table is-narrow">{{ customer.last_name }}</td>
                        <td class="table is-narrow">{{ customer.email }}</td>
                        <td class="table is-narrow">{{ customer.address }}</td>
                        <td class="table is-narrow">{{ customer.city }}</td>
                        <td class="table is-narrow">{{ customer.country }}</td>
                        <td class="table is-narrow"><router-link :to="{ name: 'Customer', params: { id: customer.id }}" class="button is-info">View</router-link>
                        <router-link :to="{ name: 'CustomerEdit', params: { id: customer.id }}" class="button is-link">Edit</router-link>
                        <router-link :to="{ name: 'CustomerDelete', params: { id: customer.id }}"  class="button is-danger">Delete</router-link></td>
                    </tr>
                    </tbody>
                </table>
              </div>
           <Paginator :last-page="lastPage" @page-changed="load($event)"/>
            </div>
        </div>
    </div>
</template>

<script>
import {ref, onMounted} from 'vue';
import axios from 'axios'
import Paginator from '@/components/paginators/Paginator'

export default {
    name: 'Customers',
    components: {Paginator},
  setup() {
    const customers = ref([]);
    const lastPage = ref(0);
    const load = async (page = 1) => {
      const response = await axios.get(`api/v1/customers/?page=${page}`);
      customers.value = response.data.data;
      lastPage.value = response.data.meta.last_page;
    }
    onMounted(load);
      
    
    return {
      customers,
      lastPage,
      load
    }
  }
}
/* To do 1 : Add search functionality
To do 2 : Rework the delete function
To do 3 : Add the dbvehicle relationship
To do 4: Swap to mysql
To do 5: Improve pagination
To do 6: Improve the ui */
</script>

<style lang="scss" scoped>

</style>