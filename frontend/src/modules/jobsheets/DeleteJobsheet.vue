<template>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'


export default {
    name: 'JobsheetDelete',

    mounted() {
        this.deleteJobsheet()
    },
    methods: {
        deleteJobsheet() {
            const jobsheetID = this.$route.params.id
            if (confirm('Are you sure you want to delete this jobsheet?')){
            axios
                .delete(`/api/v1/jobsheets/${jobsheetID}`)
                .then(response => {
                    toast({
                        message: 'The jobsheet has been removed',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })                 
                    this.$router.push('/jobsheets')
                
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })}
        }
    }
}
</script>