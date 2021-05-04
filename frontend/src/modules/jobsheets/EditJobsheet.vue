<template>
    <div class="page-edit-jobsheet">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/jobsheets">Jobsheets</router-link></li>
                <li><router-link :to="{ name: 'Jobsheet', params: { id: jobsheet.id }}">Job {{ jobsheet.reference_number }}</router-link></li>
                <li class="is-active"><router-link :to="{ name: 'JobsheetEdit', params: { id: jobsheet.id }}" aria-current="true">Edit</router-link></li>
            </ul>
        </nav>
    
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit - Job {{ jobsheet.reference_number }}</h1>
            </div>

            <div class="column is-6">
                <div class="field">
                <div class="field">
                    <label>Ref Number</label>
                    
                    <div class="control">
                        <input type="number" name="reference_number" class="input" v-model="reference_number">
                    </div>
                </div>
Select Customer<br>

<div class="select is-link">
    
  <select v-model="customer" @click="getCustomer">

    <option v-for="customer in customerget"  v-bind:key="customer.id" :value="customer.id">{{customer.first_name}} {{ customer.last_name}}</option>
  </select>
</div><br>
Select Vehicle<br>

<div class="select is-link">
    
  <select v-model="vehicle" @click="getVehicle">

    <option v-for="vehicle in vehicleget"  v-bind:key="vehicle.id" :value="vehicle.id">{{vehicle.vehicleregistrationnumber}}</option>
  </select>
</div>


                <div class="field">
                    <label>Note</label>
                    
                    <div class="control">
                        <input type="text" name="notes" class="input" v-model="notes">
                    </div>
                </div>

                <div class="field">
                    <label>Date Due</label>
                    
                    <div class="control">
                        <input type="date" name="datedue" v-model="datedue">
                    </div>
                </div>

                <div class="select">
                <select v-model="status">
                    <option>Status</option>
                    <option>Pending</option>
                    <option>Complete</option>
                </select>
                </div>

                <div class="field">
                    <label>Remaining</label>
                    
                    <div class="control">
                        <input type="number" name="remaining" class="input" v-model="remaining">
                    </div>
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
    </div>
</template>

<script>
import axios from 'axios';
import {ref, onMounted} from 'vue';
import {useRouter, useRoute} from 'vue-router';
import { toast } from 'bulma-toast';

export default {
    name: 'EditJobsheet',

    setup(){
        const router = useRouter();
        const jobsheet = ref({});
        const reference_number = ref(0);
        const customer = ref(0);
        const vehicle = ref(0);
        const status = ref('');
        const remaining = ref('');
        const notes = ref('');
        const datedue = ref(new Date())
        const {params} = useRoute();
        const customerget = ref([])

    const getCustomer = async () => {
      const response = await axios.get(`api/v1/getowners`);
      customerget.value = response.data;}

    const vehicleget = ref([])

    const getVehicle = async () => {
      const response = await axios.get(`api/v1/getvehicles`);
      vehicleget.value = response.data;}


        const SubmitForm = async() =>{
            await axios.patch(`/api/v1/jobsheets/${params.id}/`,
            {
                reference_number: reference_number.value,
                customer: customer.value,
                vehicle: vehicle.value,
                status: status.value,
                remaining: remaining.value,
                notes: notes.value,
                datedue: datedue.value
                
            }); 
            //Toast:      
            toast({
                    message: 'The job was added',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                    })
             // Toast end //
          await router.push('/jobsheets')
        }
             onMounted(async () => {
      const response = await axios.get(`api/v1/jobsheets/${params.id}`);
       jobsheet.value = response.data;
      reference_number.value = jobsheet.value.reference_number;
      notes.value = jobsheet.value.notes;
      datedue.value = jobsheet.value.datedue;
      remaining.value = jobsheet.value.remaining;
    });
              return{
            SubmitForm,
            vehicleget,
            reference_number,
            customer,
            vehicle,
            status,
            remaining,
            notes,
            datedue,
            getCustomer,
            getVehicle,
            jobsheet,
            customerget
        }
      }
    
}
</script>