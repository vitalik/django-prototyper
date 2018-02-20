<template>
    <div class="card">
        <strong class="card-header">Meta</strong>
        <div class="card-body">
            <pre>
abstract
proxy
managed


ordering
order_with_respect_to
get_latest_by

indexes
unique_together
index_together


verbose_name
verbose_name_plural


app_label
db_table


base_manager_name

db_tablespace
default_manager_name
default_related_name

            </pre>
        </div>
    </div>
</template>

<script>



export default {
    name: 'meta-editor',
    props: {
        model: {
            required: true,
            type: Object
        }
    }
}
</script>

