<template>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'


export default {
    name: 'VehicleDelete',

    mounted() {
        this.deleteVehicle()
    },
    methods: {
        deleteVehicle() {
            const vehicleID = this.$route.params.id
            if (confirm('Are you sure you want to delete this vehicle?')){
            axios
                .delete(`/api/v1/vehicles/${vehicleID}`)
                .then(response => {
                    toast({
                        message: 'The vehicle has been removed',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })                 
                    this.$router.push('/vehicles')
                
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })}
        }
    }
}
</script>