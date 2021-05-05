<template>
    <div class="page-add-vehicle">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">{{ $t("Dashboard") }}</router-link></li>
                <li><router-link to="/dashboard">{{ $t("Vehicles") }}</router-link></li>
                <li><router-link :to="{ name: 'Vehicle', params: { id: vehicle.id }}">{{ vehicle.make }} {{  vehicle.model}}</router-link></li>
                <li class="is-active"><router-link :to="{ name: 'VehicleEdit', params: { id: vehicle.id }}" aria-current="true">{{ $t("Edit") }}</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ $t("Edit") }} - {{ vehicle.make }} {{  vehicle.model}}</h1>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>{{ $t("Make") }}</label>
                    
                    <div class="control">
                        <input type="text" name="make" class="input" v-model="vehicle.make">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Model") }}</label>
                    
                    <div class="control">
                        <input type="text" name="model" class="input" v-model="vehicle.model">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Vehicleregistrationnumber") }}</label>
                    
                    <div class="control">
                        <input type="email" name="vehicleregistrationnumber" class="input" v-model="vehicle.vehicleregistrationnumber">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Fuel Type") }}</label>
                    
                    <div class="control">
                        <input type="text" name="fueltype" class="input" v-model="vehicle.fueltype">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Colour") }}</label>
                    
                    <div class="control">
                        <input type="text" name="colour" class="input" v-model="vehicle.colour">
                    </div>
                </div>
            </div>

            <div class="column is-6">
                {{ $t("Select Owner") }}<br>
<div class="select is-link" >
  <select v-model="owner" @click="getOwner">
        

    <option v-for="owner in ownerget"  v-bind:key="owner.id" :value="owner.id">{{owner.first_name}} {{ owner.last_name}}</option>
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
//I used composition API here because it's easier to implement the owner
import axios from 'axios';
import {ref, onMounted} from 'vue';
import {useRoute, useRouter} from "vue-router";
import { toast } from 'bulma-toast';

export default {
    name: 'EditVehicle',

    setup(){
        const make = ref('');
        const model = ref('');
        const vehicleregistrationnumber = ref('');
        const fueltype = ref('');
        const colour = ref('');
        const owner = ref(0);
        const vehicle = ref({});
        const router = useRouter();
        const {params} = useRoute();

        // Ref to get customers
        const ownerget = ref([])

    const getOwner = async () => {
      const response = await axios.get(`api/v1/getowners`);
      ownerget.value = response.data;
      console.log(owner.value)  }
       


        const SubmitForm = async() =>{
            await axios.patch(`/api/v1/vehicles/${params.id}/`,
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

     onMounted(async () => {
      const response = await axios.get(`api/v1/vehicles/${params.id}`);
       vehicle.value = response.data;
      make.value = vehicle.value.make;
      model.value = vehicle.value.model;
      vehicleregistrationnumber.value = vehicle.value.vehicleregistrationnumber;
      fueltype.value = vehicle.value.fueltype;
      colour.value = vehicle.value.colour;
    });

    return {
        make,model,vehicleregistrationnumber,fueltype,colour,
        vehicle, getOwner, ownerget, SubmitForm, owner
    }
    }
}

/* To Do here:
fix Select owner
Change styles */
</script>