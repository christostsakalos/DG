<template>
    <div class="page-add-subcategory">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add subcategory</h1>
            </div>
            <div class="column is-6">
                <div class="field">
                    <label>Name</label>
                    
                    <div class="control">
                        <input type="text" name="name" class="input" v-model="name">
                    </div>
                </div>

Select Parent<br>

<div class="select is-link" >
  <select v-model="parent" @click="getParent">
        

    <option v-for="parent in parentget"  v-bind:key="parent.id" :value="parent.id">{{parent.name}}</option>
  </select>
</div>

            </div>
 
            <div class="column is-12">
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click.prevent="SubmitForm">Submit</button>
                    </div>
              
                </div>
              
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import {ref, onMounted} from 'vue';
import {useRouter} from 'vue-router';
import { toast } from 'bulma-toast'

export default {
    name: 'AddVehicle',
    
    setup(){
        const router = useRouter();
        const name = ref('');
        const parent = ref(0)


        const parentget = ref([])

    const getParent = async () => {
      const response = await axios.get(`api/v1/getparents`);
      parentget.value = response.data;
      console.log(parentget.value)   }
       


        const SubmitForm = async() =>{
            await axios.post('/api/v1/subcategories/',
            {
                name: name.value,
                parent: parent.value,
                
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
            await router.push('/vehicles')
        }
        return{
            SubmitForm,
            getParent,
            parent,
            name,
            parentget
        }
    },
}
</script>

<style scoped>

</style>