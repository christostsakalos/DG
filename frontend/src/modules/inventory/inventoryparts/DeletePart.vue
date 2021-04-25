<template>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'


export default {
    name: 'PartDelete',

    mounted() {
        this.deletePart()
    },
    methods: {
        deletePart() {
            const partID = this.$route.params.id
            if (confirm('Are you sure you want to delete this part?')){
            axios
                .delete(`/api/v1/parts/${partID}`)
                .then(response => {
                    toast({
                        message: 'The part has been removed',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })                 
                    this.$router.push('/parts')
                
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })}
        }
    }
}
</script>