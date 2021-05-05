<template>
    <div class="page-add-customer">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ $t("Add customer") }}</h1>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>{{ $t("Reference Number") }}</label>
                    
                    <div class="control">
                        <input type="number" name="reference_number" class="input" v-model="customer.reference_number">
                    </div>
                </div>


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
                    <label>Email</label>
                    
                    <div class="control">
                        <input type="email" name="email" class="input" v-model="customer.email">
                    </div>
                </div>

                <div class="field">
                    <label>{{ $t("Address") }}</label>
                    
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
            </div>

            <div class="column is-12">
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="submitForm">Submit</button>
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
    name: 'AddCustomer',
    data() {
        return {
            customer: {}
        }
    },
    methods: {
        submitForm() {
            axios
                .post("/api/v1/customers/", this.customer)
                .then(response => {
                    toast({
                        message: 'The customer was added',
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