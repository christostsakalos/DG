<template>


                  <div class="table-container">
                <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                    <thead>
                    <tr>
                        <th >Name</th>
                        <th>Action</th>
                    </tr></thead>
                    <tbody v-for="category in categories" v-bind:key="category.id">
                        <tr>
                            <td>{{category.name}}</td>
                            <td><router-link :to="{ name: 'Subcategory', params: { id: category.id }}" class="button is-info">View</router-link>
                        <router-link :to="{ name: 'SubcategoryEdit', params: { id: category.id }}" class="button is-link">Edit</router-link><button class="button is-danger" @click="Deletecategory(category.id)">Delete</button></td>
                        </tr>
                        
                    </tbody>
                    <Paginator :last-page="lastPage" @page-changed="load($event)"/>
                </table>
                  </div>

</template>


<script>
import {ref, onMounted} from 'vue'
import axios from 'axios'
import Paginator from '@/components/paginators/Paginator'
export default {
    name: 'Subcategories',
    components: {Paginator},
    setup(){
        const categories = ref([]);
        const lastPage = ref(0);


        const load = async (page = 1) => {
            const response = await axios.get(`api/v1/subcategories/?page=${page}`);
            categories.value = response.data.data
            lastPage.value = response.data.meta.last_page

            console.log(categories.value)
        }
        async function Deletecategory (id = category.id) {
      if (confirm('Are you sure you want to delete this record?')) {
           await axios.delete(`/api/v1/subcategories/${id}`);
            categories.value = categories.value.filter((categories)=> categories.id !== id)
            toast({
                        message: 'The category has been removed',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })    
                     }
               
                  }
  
        onMounted(load)
        return {categories, load,
        lastPage, Deletecategory
        }

    },
}
</script>

<style scoped>

</style>