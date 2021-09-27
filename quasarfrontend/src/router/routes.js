const routes = [{
        path: '/',
        component: () =>
            import ('layouts/MainLayout.vue'),
        children: [{
                path: '',
                component: () =>
                    import ('pages/Index.vue')
            },
            {
                path: 'customers',
                component: () =>
                    import ('pages/Customers.vue')
            },
            {
                path: 'vehicles',
                component: () =>
                    import ('pages/Vehicles.vue')
            },
            {
                path: 'jobsheets',
                component: () =>
                    import ('pages/Jobsheets.vue')
            }
        ]
    },

    // Always leave this as last one,
    // but you can also remove it
    {
        path: '/:catchAll(.*)*',
        component: () =>
            import ('pages/Error404.vue')
    }
]

export default routes