<template>
    <div class="page-edit-customer">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">{{ $t("Dashboard") }}</router-link></li>
                <li><router-link to="/customers">{{ $t("Customers") }}</router-link></li>
                <li><router-link :to="{ name: 'Customer', params: { id: customer.id }}">{{ customer.first_name }} {{  customer.last_name}}</router-link></li>
                <li class="is-active"><router-link :to="{ name: 'CustomerEdit', params: { id: customer.id }}" aria-current="true">{{ $t("Edit") }}</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ $t("Edit") }} - {{ customer.first_name }} {{  customer.last_name}}</h1>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>{{ $t("First Name") }}</label>
                    
                    <div class="control">
                        <input type="text" name="first_name" class="input" v-model="customer.first_name">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Last Name") }}</label>
                    
                    <div class="control">
                        <input type="text" name="last_name" class="input" v-model="customer.last_name">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Email") }}</label>
                    
                    <div class="control">
                        <input type="email" name="email" class="input" v-model="customer.email">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Address") }} </label>
                    
                    <div class="control">
                        <input type="text" name="address" class="input" v-model="customer.address">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("City") }}</label>
                    
                    <div class="control">
                        <input type="text" name="city" class="input" v-model="customer.city">
                    </div>
                </div>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>{{ $t("Postcode") }}</label>
                    
                    <div class="control">
                        <input type="text" name="postcode" class="input" v-model="customer.postcode">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Country") }}</label>
                    
                    <div class="control">
                        <input type="text" name="country" class="input" v-model="customer.country">
                    </div>
                </div>
            </div>

            <div class="column is-12">
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="submitForm">Save changes</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'EditCustomer',
    data() {
        return {
            customer: {}
        }
    },
    mounted() {
        this.getCustomer()
    },
    methods: {
        getCustomer() {
            const customerID = this.$route.params.id

            axios
                .get(`/api/v1/customers/${customerID}`)
                .then(response => {
                    this.customer = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        submitForm() {
            const customerID = this.$route.params.id

            axios
                .patch(`/api/v1/customers/${customerID}/`, this.customer)
                .then(response => {
                    toast({
                        message: 'The changes was saved',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                    
                    this.$router.push('/customers')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>