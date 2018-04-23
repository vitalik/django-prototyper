<template>
    <div>

        <div class="heading">
            <div class="container-fluid">
                <h2>Admin - {{app.name}}.{{model.name}}</h2>
            </div>
        </div>

        <div class="container-fluid">
            <div class="row">
                <div class="col-md-6">
                    <SelectFields attribute="list_display" :model="model" class="mt-1"></SelectFields>
                    <SelectFields attribute="list_display_links" :model="model" class="mt-1"></SelectFields>
                    <SelectFields attribute="list_editable" :model="model" class="mt-1"></SelectFields>
                    <SelectFields attribute="list_filter" :model="model" class="mt-1"></SelectFields>
                    <SelectFields attribute="search_fields" :model="model" class="mt-1"></SelectFields>
                    <SelectFields attribute="date_hierarchy" :single="true" :model="model" class="mt-1"></SelectFields>
                </div>
                <div class="col-md-6">
                    <SelectFields attribute="radio_fields" :model="model" class="mt-1"></SelectFields>
                    <SelectFields attribute="raw_id_fields" :model="model" class="mt-1"></SelectFields>
                    <SelectFields attribute="autocomplete_fields" :model="model" class="mt-1"></SelectFields>
                    <SelectFields attribute="readonly_fields" :model="model" class="mt-1"></SelectFields>
                    <SelectFields attribute="filter_horizontal" :model="model" class="mt-1"></SelectFields>
                    <SelectFields attribute="filter_vertical" :model="model" class="mt-1"></SelectFields>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { store } from '../../store'

import SelectFields from './SelectFields'

export default {
    name: 'Editor',
    data() {
        return {
        }
    },
    computed: {
        app() {
            return store.app_get(this.$route.params.app)
        },
        model() {
            return store.models_get(this.app.name, this.$route.params.model)
        }
    },
    methods: {
        // XXX(e) {
        // }
    },
    components: {
        SelectFields
    }
}
</script>
