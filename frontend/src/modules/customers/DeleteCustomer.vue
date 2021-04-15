<template>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'


export default {
    name: 'CustomerDelete',

    mounted() {
        this.deleteCustomer()
    },
    methods: {
        deleteCustomer() {
            const customerID = this.$route.params.id
            if (confirm('Are you sure you want to delete this customer?')){
            axios
                .delete(`/api/v1/customers/${customerID}`)
                .then(response => {
                    toast({
                        message: 'The customer has been removed',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })                 
                    this.$router.push('/customers')
                
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })}
        }
    }
}
</script>