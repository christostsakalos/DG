<template>
    <div class="page-add-vehicle">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add vehicle</h1>
            </div>
            <div class="column is-6">
                <div class="field">
                    <label>Make</label>
                    
                    <div class="control">
                        <input type="text" name="make" class="input" v-model="make">
                    </div>
                </div>


                <div class="field">
                    <label>Model</label>
                    
                    <div class="control">
                        <input type="text" name="model" class="input" v-model="model">
                    </div>
                </div>

                <div class="field">
                    <label>Vehicle Registration Number</label>
                    
                    <div class="control">
                        <input type="text" name="vehicleregistrationnumber" class="input" v-model="vehicleregistrationnumber">
                    </div>
                </div>

                <div class="field">
                    <label>Fuel Type</label>
                    
                    <div class="control">
                        <input type="text" name="fueltype" class="input" v-model="fueltype">
                    </div>
                </div>

                <div class="field">
                    <label>Colour</label>
                    
                    <div class="control">
                        <input type="text" name="colour" class="input" v-model="colour">
                    </div>
                </div>
Select Owner<br>

<div class="select is-link">
    
  <select v-model="owner" @click="getOwner">

    <option v-for="owner in ownerget"  v-bind:key="owner.id" :value="owner.id">{{owner.first_name}} {{ owner.last_name}}</option>
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
        const make = ref('');
        const model = ref('');
        const vehicleregistrationnumber = ref('');
        const fueltype = ref('');
        const colour = ref('');
        const owner = ref(0)

        // Ref to get customers
        const ownerget = ref([])

    const getOwner = async () => {
      const response = await axios.get(`api/v1/getowners`);
      ownerget.value = response.data;
      console.log(ownerget.value)   }
       


        const SubmitForm = async() =>{
            await axios.post('/api/v1/vehicles/',
            {
                make: make.value,
                model: model.value,
                vehicleregistrationnumber: vehicleregistrationnumber.value,
                fueltype: fueltype.value,
                colour: colour.value,
                owner: owner.value,
                
            }); 
            //Toast:      
            toast({
                    message: 'The customer was added',
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
            make,
            model,
            vehicleregistrationnumber,
            fueltype,
            ownerget,
            colour,
            getOwner,
            owner
        }
    },
}
</script>

<style scoped>

</style>