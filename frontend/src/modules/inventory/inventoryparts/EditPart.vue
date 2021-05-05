<template>
    <div class="page-edit-part">
        <Languages />
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">{{ $t("Dashboard") }}</router-link></li>
                <li><router-link to="/parts">{{ $t("Parts") }}</router-link></li>
                <li><router-link :to="{ name: 'Part', params: { id: part.id }}">{{ part.name }} {{  part.description}}</router-link></li>
                <li class="is-active"><router-link :to="{ name: 'PartEdit', params: { id: part.id }}" aria-current="true">{{ $t("Edit") }}</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ $t("Edit") }} - {{part.name}}</h1>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>{{ $t("Name") }}</label>
                    
                    <div class="control">
                        <input type="text" name="name" class="input" v-model="part.name">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Description") }}</label>
                    
                    <div class="control">
                        <input type="text" name="description" class="input" v-model="part.description">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Quantity") }}</label>
                    
                    <div class="control">
                        <input type="number" name="quantity" class="input" v-model="part.quantity">
                    </div>
                </div>
            </div>

            <div class="column is-6">
                {{ $t("Select Category") }}<br>
<div class="select is-link" >
  <select v-model="category" @click="getCategory">
        

    <option v-for="category in categoryget"  v-bind:key="category.id" :value="category.id">{{category.name}}</option>
  </select>
</div>
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
</template>

<script>
//I used composition API here because it's easier to implement the category
import axios from 'axios';
import {ref, onMounted} from 'vue';
import {useRoute, useRouter} from "vue-router";
import { toast } from 'bulma-toast';
import Languages from '@/components/Languages.vue';

export default {
    name: 'EditPart',
    components: {Languages},

    setup(){
        const name = ref('');
        const description = ref('');
        const quantity = ref(0);
        const category = ref(0);
        const part = ref({});
        const router = useRouter();
        const {params} = useRoute();

        // Ref to get customers
        const categoryget = ref([])

    const getCategory = async () => {
      const response = await axios.get(`api/v1/getcategories`);
      categoryget.value = response.data;
      console.log(category.value)  }
       


        const SubmitForm = async() =>{
            await axios.patch(`/api/v1/parts/${params.id}/`,
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

     onMounted(async () => {
      const response = await axios.get(`api/v1/parts/${params.id}`);
       part.value = response.data;
      name.value = part.value.name;
      description.value = part.value.description;
      quantity.value = part.value.quantity;
    });

    return {
        name,description,quantity,
        part, getCategory, categoryget, SubmitForm, category
    }
    }
}

/* To Do here:
fix Select category
Change styles */
</script>