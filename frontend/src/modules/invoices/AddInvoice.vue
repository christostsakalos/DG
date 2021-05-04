<template>
    <div class="page-add-invoice">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/invoices">Invoices</router-link></li>
                <li class="is-active"><router-link to="/invoices/add" aria-current="true">Add</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add invoice</h1>
            </div>

            <div class="column is-12">
                <h2 class="is-size-5 mb-4">Customer</h2>

                <div class="select">
                    <select name="customer" v-model="invoice.customer">
                        <option value="">- Select customer -</option>
                        <option 
                            v-for="customer in customers"
                            v-bind:key="customer.id"
                            v-bind:value="customer"
                        >
                            {{ customer.first_name }} {{ customer.last_name }}
                        </option>
                    </select>
                </div>

                <div class="box mt-4" v-if="invoice.customer">
                    <p><strong>{{ invoice.customer.first_name}} {{invoice.customer.last_name}}</strong></p>
                    
                    <p><strong>Email:</strong> {{ invoice.customer.email }}</p>
                    <p v-if="invoice.customer.address">{{ invoice.customer.address }}</p>
                    <p v-if="invoice.customer.postcode">{{ invoice.customer.postcode }}</p>
                    <p v-if="invoice.customer.country">{{ invoice.customer.country }}</p>
                </div>
            </div>

            <div class="column is-12">
                <h2 class="is-size-5 mb-4">Items</h2>

                <ItemForm
                    v-for="item in invoice.items"
                    v-bind:key="item.item_num"
                    v-bind:initialItem="item"
                    v-on:updatePrice="updateTotals"
                >
                </ItemForm>

                <button class="button is-light" @click="addItem">+</button>
            </div>

            <div class="column is-12">
                <h2 class="is-size-5 mb-4">Misc</h2>

                <div class="field">
                    <label>Due days</label>

                    <div class="control">
                        <input type="number" class="input" v-model="invoice.due_days">
                    </div>
                </div>

                <div class="field">
                    <label>Bank Account</label>

                    <div class="control">
                        <input type="text" class="input" v-model="invoice.bankaccount">
                    </div>
                </div>
            </div>
        </div>

        <div class="column is-12">
            <h2 class="is-size-5 mb-4">Total</h2>

            <p><strong>Net amount</strong>: £{{ invoice.net_amount }}</p>
            <p><strong>Vat amount</strong>: £{{ invoice.vat_amount }}</p>
            <p><strong>Gross amount</strong>: £{{ invoice.gross_amount }}</p>
        </div>

        <div class="column is-12">
            <button class="button is-success" @click="submitForm">Save</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

import ItemForm from '@/components/ItemForm.vue'

export default {
    name: 'AddInvoice',
    components: {
        ItemForm
    },
    data() {
        return {
            invoice: {
                customer: '',
                items: [
                    {
                        item_num: 0,
                        title: '',
                        unit_price: '',
                        quantity: 1,
                        vat_rate: 0,
                        net_amount: 0
                    }
                ],
                due_days: 14, 
                net_amount: 0,
                vat_amount: 0,
                gross_amount: 0,
                bankaccount: '',
            },
            customers: []
        }
    },
    async mounted() {
        await this.getCustomers()
    },
    methods: {
        getCustomers() {
            axios
                .get('/api/v1/getowners')
                .then(response => {
                    this.customers = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        addItem() {
            this.invoice.items.push({
                item_num: this.invoice.items.length,
                title: '',
                unit_price: '',
                quantity: 1,
                vat_rate: 0,
                net_amount: 0
            })
        },
        updateTotals(changedItem) {
            let net_amount = 0
            let vat_amount = 0

            let item = this.invoice.items.filter(i => i.item_num === changedItem.item_num)

            item = changedItem

            for (let i = 0; i < this.invoice.items.length; i++) {
                const vat_rate = this.invoice.items[i].vat_rate

                vat_amount += this.invoice.items[i].net_amount * (vat_rate / 100)
                net_amount += this.invoice.items[i].net_amount
            }

            this.invoice.net_amount = net_amount
            this.invoice.vat_amount = vat_amount
            this.invoice.gross_amount = net_amount + vat_amount
            this.invoice.discount_amount = 0
        },
        submitForm() {
            this.invoice.customer = this.invoice.customer.id

            axios
                .post('/api/v1/invoices/', this.invoice)
                .then(response => {
                    toast({
                        message: 'The invoice was added',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })

                    this.$router.push('/invoices')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>

<style lang="scss">
    .select, .select select {
        width: 100%;
    }
</style>