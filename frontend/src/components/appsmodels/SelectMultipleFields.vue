<template>
    <div class="row justify-content-between align-items-baseline multiple-fields-wrapper">
        <p class="col-3"> {{attribute}}</p>
        <div class="col" style="margin: 10px">
            <div v-for="fields in multiple_fields" class="row">
                <select-fields :attribute="fields" :model="model" class="mt-1"/>
                <button @click="remove_fields(fields)" type="button" class="close" aria-label="Close">
                    <span aria-hidden="true">&times; </span>
                </button>
            </div>
        </div>
        <button @click="add_fields" type="button" class="btn add-another addlink">+</button>
    </div>
</template>

<script>
    import SelectFields from "../admin/SelectFields";

    export default {
        name: "select-multiple-fields",
        props: ['attribute', 'model'],
        data() {
            return {
                'multiple_fields': [1]
            }
        },
        methods: {
            remove_fields(field) {
                this.multiple_fields.splice(this.multiple_fields.indexOf(field), 1);
            },
            add_fields() {

                this.multiple_fields.push((_.last(this.multiple_fields) || 0) + 1);
            },
        },
        components: {SelectFields},
    }
</script>

<style scoped>
    .multiple-fields-wrapper {
        margin: 0;
        padding: 0 5px 0 5px;
        border: 1px gainsboro solid;
    }
</style>