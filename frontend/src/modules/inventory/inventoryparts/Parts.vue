<template>
    <div class="page-parts">
        <div class="columns is-multiline">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/parts">Parts</router-link></li>
            </ul>
        </nav>
            <div class="column is-12">
                <h1 class="title">Parts Manager</h1>

                <router-link :to="{ name: 'AddPart' }" class="button is-success mt-4">Add Part</router-link>
                <div class="field has-addons">
  <div class="control">
    <br>
        <input class="input" type="text" placeholder="Search a part..." v-model="search_term" @keyup="getPart">
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
                        <th >Name</th>
                        <th>Description</th>
                        <th>Quantity</th>
                        <th>Category</th>
                        <th>Action</th>
                    </tr></thead>
                    
                    <tbody v-if="search_term.length <= 3" @keyup="load">
                   
                    <tr v-for="part in parts" v-bind:key="part.id" >
                        <td class="table is-narrow">{{ part.name }}</td>
                        <td class="table is-narrow">{{ part.description }}</td>
                        <td class="table is-narrow">{{ part.quantity}}</td>
                        <td class="table is-narrow">{{ part.category_name }}</td>
                        <td class="table is-narrow"><router-link :to="{ name: 'Part', params: { id: part.id }}" class="button is-info">View</router-link>
                        <router-link :to="{ name: 'PartEdit', params: { id: part.id }}" class="button is-link">Edit</router-link>
                        <button class="button is-danger" @click="Deletepart(part.id)">Delete</button></td>
                    </tr>
                 <Paginator :last-page="lastPage" @page-changed="load($event)"/>   </tbody>
                    <tbody v-else-if="search_term.length >= 3">
                                          <tr v-for="part in searched_parts" v-bind:key="part.id">
                        <td class="table is-narrow">{{ part.name }}</td>
                        <td class="table is-narrow">{{ part.description }}</td>
                        <td class="table is-narrow">{{ part.quantity}}</td>
                        <td class="table is-narrow">{{ part.category_name }}</td>
                        <td class="table is-narrow"><router-link :to="{ name: 'Part', params: { id: part.id }}" class="button is-info">View</router-link>
                        <router-link :to="{ name: 'PartEdit', params: { id: part.id }}" class="button is-link">Edit</router-link>
                        <button class="button is-danger" @click="Deletepart(part.id)">Delete</button></td>
                    </tr>
               <PaginatorSearch :last-page="lastPagesearch" @page-changedsearch="getPart($event)" />
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
    name: 'Parts',
    components: {Paginator, PaginatorSearch},
  setup() {



    const parts = ref([]);
    const searched_parts = ref([]);
    const search_term = ref("");
    const lastPage = ref(0);
    const pagesearch = 1
    const lastPagesearch = ref(0);
    const search_results = ref([]);
    const load = async (page = 1) => {
      const response = await axios.get(`api/v1/parts/?page=${page}`);
      parts.value = response.data.data;
      lastPage.value = response.data.meta.last_page;}
    const getPart = async () => {
      const responsesearch = await axios.get(`api/v1/parts/?page=${pagesearch}&search=${search_term.value}`);
      searched_parts.value = responsesearch.data.data;
      lastPagesearch.value = responsesearch.data.meta.last_page;}

    onMounted(load);

    async function Deletepart (id = part.id) {
      if (confirm('Are you sure you want to delete this record?')) {
           await axios.delete(`/api/v1/parts/${id}`);
            parts.value = parts.value.filter((parts)=> parts.id !== id)
            toast({
                        message: 'The part has been removed',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })    
                     }
               
                  }
       
    return {
      parts,
      search_results,
      lastPage,
      lastPagesearch,
      load,
      getPart,
      search_term,
      searched_parts,
      pagesearch,
      Deletepart,

    
      
    }
  }
}
/* To do 1 : Add search functionality --- Done
To do 2 : Rework the delete function --- Done
To do 3 : Add the dbpart relationship --- Done
To do 4: Swap to mysql
To do 5: Improve pagination
To do 6: Improve the ui 
To do 7: fix the validators */
</script>

<style lang="scss" scoped>
</style>