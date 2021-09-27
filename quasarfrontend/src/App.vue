<template>
  <router-view />
</template>
<script>
import { QSpinnerHourglass, useQuasar } from 'quasar';
import { defineComponent} from 'vue';
export default defineComponent({
  name: 'App',
  setup () {
    const $q = useQuasar()
   

  $q.loadingBar.setDefaults({
    color: 'cyan',
    size: '5px',
    position: 'top'
  })
    $q.loading.setDefaults({
      spinner: QSpinnerHourglass,
      spinnerColor: 'cyan',
      spinnerSize: 140,
      delay: 300,
 
      message: 'Some important process is in progress. Hang on...',
      messageColor: 'black'
    })
    return{
      
    }
  }
})
</script>