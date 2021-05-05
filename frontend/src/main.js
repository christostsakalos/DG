import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import en from './tranlations/en.json'
import gr from './tranlations/gr.json'
import {createI18n} from "vue-i18n";

/* const messages = {
    en: en,
    gr: gr,
} */
const i18n = createI18n({
    locale: 'en',
    messages: {
        en: en,
        gr: gr
    },
    fallbackLocale: 'gr'
})



axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).use(store).use(i18n).use(router, axios).mount('#app')
