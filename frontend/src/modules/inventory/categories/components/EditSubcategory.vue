<template>
    <div class="page-edit-subcategory">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/categories">SubCategories</router-link></li>
                <li><router-link :to="{ name: 'Subcategory', params: { id: subcategory.id }}">{{ subcategory.name }}</router-link></li>
                <li class="is-active"><router-link :to="{ name: 'SubcategoryEdit', params: { id: subcategory.id }}" aria-current="true">Edit</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit - {{ subcategory.name }}</h1>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>Name</label>
                    
                    <div class="control">
                        <input type="text" name="name" class="input" v-model="subcategory.name">
                    </div>
                </div>

<div class="select is-link" >
  <select v-model="parent" @click="getParent">
        

    <option v-for="parent in parentget"  v-bind:key="parent.id" :value="parent.id">{{parent.name}}</option>
  </select>
</div>
            <div class="column is-12">
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="SubmitForm">Save changes</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios';
import {ref, onMounted} from 'vue';
import {useRoute, useRouter} from "vue-router";
import { toast } from 'bulma-toast';

export default {
    name: 'EditSubcategory',
    setup(){
        const subcategory = ref([]);
        const name = ref('');
        const parent = ref(0);
        const router = useRouter();
        const {params} = useRoute();


        const parentget = ref([])

    const getParent = async () => {
      const response = await axios.get(`api/v1/getparents`);
      parentget.value = response.data;
      console.log(parent.value)  }
       


        const SubmitForm = async() =>{
            await axios.patch(`/api/v1/subcategories/${params.id}/`,
            {
                name: name.value,
                parent: parent.value
                
                
            }); 
            //Toast:      
            toast({
                    message: 'The category was added',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                    })
             // Toast end //
            await router.push('/categories')
            }

     onMounted(async () => {
      const response = await axios.get(`api/v1/subcategories/${params.id}`);
       subcategory.value = response.data;
      name.value = subcategory.value.name;
      parent.value = subcategory.value.parent_name;
    });

    return {
        name,
        subcategory, getParent, parentget, SubmitForm, parent
    }
    }
}

/* To Do here:
fix Select parent
Change styles */
</script>