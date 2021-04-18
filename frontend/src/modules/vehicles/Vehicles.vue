<template>
    <div class="page-vehicles">
        <div class="columns is-multiline">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/vehicles">Vehicles</router-link></li>
            </ul>
        </nav>
            <div class="column is-12">
                <h1 class="title">Vehicle Manager</h1>

                <router-link :to="{ name: 'AddVehicle' }" class="button is-success mt-4">Add vehicle</router-link>
                <div class="field has-addons">
  <div class="control">
    <br>
        <input class="input" type="text" placeholder="Search a vehicle..." v-model="search_term" @keyup="getVehicle">
  </div>
  <div class="control">
    <br>
  </div>
</div>
            </div>

            <div
                class="column is-8">
              <div class="table-container">
                <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                    <thead>
                    <tr class="th">
                        <th >Make</th>
                        <th>Model</th>
                        <th>Vehicle Registration Number</th>
                        <th>Fuel Type</th>
                        <th>Colour</th>
                        <th>Owner</th>
                        <th>Action</th>
                    </tr></thead>
                    
                    <tbody v-if="search_term.length <= 3" @keyup="load">
                   
                    <tr v-for="vehicle in vehicles" v-bind:key="vehicle.id" >
                        <td class="table is-narrow">{{ vehicle.make }}</td>
                        <td class="table is-narrow">{{ vehicle.model }}</td>
                        <td class="table is-narrow">{{ vehicle.vehicleregistrationnumber}}</td>
                        <td class="table is-narrow">{{ vehicle.fueltype }}</td>
                        <td class="table is-narrow">{{ vehicle.colour }}</td>
                        <td class="table is-narrow">{{ vehicle.first_name }} {{vehicle.last_name}}</td>
                        <td class="table is-narrow"><router-link :to="{ name: 'Vehicle', params: { id: vehicle.id }}" class="button is-info">View</router-link>
                        <router-link :to="{ name: 'VehicleEdit', params: { id: vehicle.id }}" class="button is-link">Edit</router-link>
                        <button class="button is-danger" @click="Deletevehicle(vehicle.id)">Delete</button></td>
                    </tr>
                 <Paginator :last-page="lastPage" @page-changed="load($event)"/>   </tbody>
                    <tbody v-else-if="search_term.length >= 3">
                                          <tr v-for="vehicle in searched_vehicles" v-bind:key="vehicle.id">
                        <td class="table is-narrow">{{ vehicle.make }}</td>
                        <td class="table is-narrow">{{ vehicle.model }}</td>
                        <td class="table is-narrow">{{ vehicle.vehicleregistrationnumber}}</td>
                        <td class="table is-narrow">{{ vehicle.fueltype }}</td>
                        <td class="table is-narrow">{{ vehicle.colour }}</td>
                        <td class="table is-narrow">{{ vehicle.first_name }} {{vehicle.last_name}}</td>
                        <td class="table is-narrow"><router-link :to="{ name: 'vehicle', params: { id: vehicle.id }}" class="button is-info">View</router-link>
                        <router-link :to="{ name: 'VehicleEdit', params: { id: vehicle.id }}" class="button is-link">Edit</router-link>
                        <button class="button is-danger" @click="Deletevehicle(vehicle.id)">Delete</button></td>
                    </tr>
               <PaginatorSearch :last-page="lastPagesearch" @page-changedsearch="getVehicle($event)" />
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
    name: 'Vehicles',
    components: {Paginator, PaginatorSearch},
  setup() {



    const vehicles = ref([]);
    const searched_vehicles = ref([]);
    const search_term = ref("");
    const lastPage = ref(0);
    const pagesearch = 1
    const lastPagesearch = ref(0);
    const search_results = ref([]);
    const load = async (page = 1) => {
      const response = await axios.get(`api/v1/vehicles/?page=${page}`);
      vehicles.value = response.data.data;
      lastPage.value = response.data.meta.last_page;}
    const getVehicle = async () => {
      const responsesearch = await axios.get(`api/v1/vehicles/?page=${pagesearch}&search=${search_term.value}`);
      searched_vehicles.value = responsesearch.data.data;
      lastPagesearch.value = responsesearch.data.meta.last_page;}

    onMounted(load);

    async function Deletevehicle (id = vehicle.id) {
      if (confirm('Are you sure you want to delete this record?')) {
           await axios.delete(`/api/v1/vehicles/${id}`);
            vehicles.value = vehicles.value.filter((vehicles)=> vehicles.id !== id)
            toast({
                        message: 'The vehicle has been removed',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })    
                     }
               
                  }
       
    return {
      vehicles,
      search_results,
      lastPage,
      lastPagesearch,
      load,
      getVehicle,
      search_term,
      searched_vehicles,
      pagesearch,
      Deletevehicle,

    
      
    }
  }
}
/* To do 1 : Add search functionality --- Done
To do 2 : Rework the delete function --- Done
To do 3 : Add the dbvehicle relationship --- Done
To do 4: Swap to mysql
To do 5: Improve pagination
To do 6: Improve the ui 
To do 7: fix the validators */
</script>

<style lang="scss" scoped>
</style>