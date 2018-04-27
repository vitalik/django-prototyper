<template>
    <div class="card">
        <div class="card-body">
            <strong>Meta</strong>
            <hr>

            <check-label v-model="abstract" label="abstract" :initial="false"/>
            <check-label v-model="proxy" label="proxy" :initial="false"/>
            <check-label v-model="managed" label="managed" :initial="true"/>

            <!--

            <select-negative-fields attribute="ordering" :model="model" class="mt-1"/>
            <select-negative-fields attribute="get_latest_by" :model="model" class="mt-1"/>

            <select-multiple-fields attribute="indexes" :model="model" class="mt-1"/>
            <select-multiple-fields attribute="unique_together" :model="model" class="mt-1"/>

            -->

<!--
// empty-by-default string attrs
order_with_respect_to
verbose_name
verbose_name_plural
app_label
db_table
base_manager_name
db_tablespace
default_manager_name
default_related_name
-->

        </div>
    </div>
</template>

<script>

    import CheckLabel from '../utils/CheckLabel'
    import SelectNegativeFields from "./SelectOrderableFields";
    import SelectMultipleFields from "./SelectMultipleFields";

    export default {
        name: 'meta-editor',
        props: {
            model: {
                required: true,
                type: Object
            }
        },
        data() {
            return {
                abstract: false,
                managed: true,
                proxy: false,
            }
        },
        components: {
            SelectMultipleFields,
            SelectNegativeFields,
            CheckLabel,
        }
    }
</script>

