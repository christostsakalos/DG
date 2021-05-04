<template>
    <div class="page-invoicesdel">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li class="is-active"><router-link to="/invoicesdel" aria-current="true">Invoices</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Invoices</h1>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Invoice Number</th>
                            <th>Customer</th>
                            <th>Amount</th>
                            <th>Due date</th>
                            <th>Is paid</th>
                            <th>Action</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="invoice in invoices"
                            v-bind:key="invoice.id"
                        >
                            <td>{{ invoice.id }}</td>
                            <td>{{ invoice.first_name }}{{ invoice.last_name}}</td>
                            <td>{{ invoice.gross_amount }}</td>
                            <td>{{ invoice.get_due_date_formatted }}</td>
                            <td>{{ getStatusLabel(invoice) }}</td>
                            <td>
                                <button class="button is-danger" @click="Deleteinvoice(invoice.id)">Delete</button>
                            </td>
                        </tr>
                       <div v-if="invoices.length > 15"> <Paginator :last-page="lastPage"  @page-changed="load($event)"/> </div>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import {ref, onMounted} from 'vue';
import Paginator from '@/components/paginators/Paginator'

export default {
    name: 'Invoicesdelete',
    components: {Paginator},

    setup(){
        const invoices = ref([]);
        const lastPage = ref(0);
        
        const load = async (page = 1) => {
            const response = await axios.get(`api/v1/invoices/?page=${page}`);
            invoices.value = response.data.data;
            lastPage.value = response.data.meta.last_page;}

        function getStatusLabel(invoice) {
            if (invoice.is_paid) {
                return 'Yes'
            } else {
                return 'No'
            }
        }

        onMounted(load);
    async function Deleteinvoice (id = invoice.id) {
      if (confirm('Are you sure you want to delete this invoice?')) {
           await axios.delete(`/api/v1/invoices/${id}`);
            invoices.value = invoices.value.filter((invoices)=> invoices.id !== id)
            toast({
                        message: 'The customer has been removed',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })    
                     }
               
                  }

        return{
            invoices,
            lastPage,
            load,
            getStatusLabel,
            Deleteinvoice
        }

    }
}
</script>