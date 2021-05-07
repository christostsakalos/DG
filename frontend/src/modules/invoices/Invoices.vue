<template>
    <div class="page-invoices">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">{{ $t("Dashboard") }}</router-link></li>
                <li class="is-active"><router-link to="/invoices" aria-current="true" >{{ $t("Invoices") }}</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ $t("Invoices") }}</h1>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th><p>{{ $t("Invoice Number") }}</p></th>
                            <th>{{ $t("Customer") }}</th>
                            <th>{{ $t("Amount") }}</th>
                            <th>{{$t("Due date")}}</th>
                            <th>{{ $t("Is paid") }}</th>
                            <th>{{ $t("Action") }}</th>
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
                            <td v-if="invoice.is_paid === false">{{ invoice.get_due_date_formatted }}</td><td v-else></td>
                            <td>{{ getStatusLabel(invoice) }}</td>
                            <td>
                                <router-link class="button is-link" :to="{ name: 'Invoice', params: { id: invoice.id }}">{{ $t("Details") }}</router-link>
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
import {ref, onMounted} from 'vue';
import Paginator from '@/components/paginators/Paginator'

export default {
    name: 'Invoices',
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


        return{
            invoices,
            lastPage,
            load,
            getStatusLabel
        }

    }
}
</script>