<template>
    <div class="page-add-part">
         <Languages /><br>
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ $t("Add Part") }}</h1>
            </div>
            <div class="column is-6">
                <div class="field">
                    <label>{{ $t("Name") }}</label>
                    
                    <div class="control">
                        <input type="text" name="name" class="input" v-model="name">
                    </div>
                </div>


                <div class="field">
                    <label>{{ $t("Description") }}</label>
                    
                    <div class="control">
                        <input type="text" name="description" class="input" v-model="description">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Quantity") }}</label>
                    
                    <div class="control">
                        <input type="number" step="0.01" class="input" v-model="quantity">
                    </div>
                </div>

                </div>
{{ $t("Select Category") }}<br>

<div class="select is-link">
    
  <select v-model="category" @click="getCategory">

    <option v-for="category in categoryget"  v-bind:key="category.id" :value="category.id">{{category.name}}</option>
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
</template>

<script>
import axios from 'axios'
import {ref, onMounted} from 'vue';
import {useRouter} from 'vue-router';
import { toast } from 'bulma-toast';
import Languages from '@/components/Languages.vue';

export default {
    name: 'AddPart',
    components: {Languages},
    
    setup(){
        const router = useRouter();
        const name = ref('');
        const description = ref('');
        const quantity = ref(0);
        const category = ref(0)

        // Ref to get customers
        const categoryget = ref([])

    const getCategory = async () => {
      const response = await axios.get(`api/v1/getcategories`);
      categoryget.value = response.data;}
       


        const SubmitForm = async() =>{
            await axios.post('/api/v1/parts/',
            {
                name: name.value,
                description: description.value,
                quantity: quantity.value,
                category: category.value,
                
            }); 
            //Toast:      
            toast({
                    message: 'The part was added',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                    })
             // Toast end //
            await router.push('/parts')
        }
        return{
            SubmitForm,
            name,
            description,
            quantity,
            category,
            categoryget,
            getCategory,
        }
    },
}
</script>

<style scoped>

</style>