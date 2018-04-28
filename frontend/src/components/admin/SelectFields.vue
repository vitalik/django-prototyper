<template>
    <div class="card card-body">

        <div class="row">
            <div class="col-4 text-nowrap">
                {{ attribute }}
            </div>
            <div class="col" v-click-outside="on_outside_click">

                <draggable :list="selected_fields" element="span">
                    <a v-for="fld in selected_fields"
                       @click="toggle_field(fld)"
                       class="badge badge-secondary mr-1"
                       href="javascript:void(0)">
                        {{ fld }}
                    </a>
                </draggable>

                <a @click="edit_mode = true" class="badge badge-light mr-1" href="javascript:void(0)">select...</a>

                <div v-if="edit_mode" class="card card-body mt-1"
                     style="position: absolute; width: 340px; z-index: 1000;">
                    <div>
                        <button @click="edit_mode = false" type="button" class="close" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>

                        Select fields:

                        <div v-for="fld in available_fields">
                            <a @click="toggle_field(fld.name)"
                               :class="{'badge-secondary': fld.selected, 'badge-light': !fld.selected}"
                               class="badge mr-1"
                               href="javascript:void(0)">
                                {{ fld.name }}
                            </a>
                        </div>
                        <button v-if="!single"
                                @click="select_all"
                                :class="{'hidden': unselected_fields.length == 0}"
                                class="btn btn-link btn-sm">
                            Select all...
                        </button>
                    </div>
                </div>
            </div>
        </div>


    </div>
</template>

<script>

    import _ from 'lodash'
    import draggable from 'vuedraggable'

    export default {
        name: 'SelectFields',
        props: ['model', 'attribute', 'single'],
        data() {
            let fields = [];
            if (this.model['admin'] && this.model['admin'][this.attribute] && this.model['admin'][this.attribute]['fields']) {
                fields = this.model['admin'][this.attribute]['fields']
            }
            return {
                selected_fields: fields,
                edit_mode: false,
            }
        },
        mounted() {
            this.$set(this.model['admin'], this.attribute, {});
            this.$set(this.model['admin'][this.attribute], "single", this.single || false);
            this.$set(this.model['admin'][this.attribute], "fields", this.selected_fields);
        },
        computed: {
            applicable_fields() {
                // TODO: based on attribute
                return _.map(this.model.fields, 'name')
            },
            available_fields() {
                return _.map(this.applicable_fields, function (name) {
                    return {
                        name,
                        'selected': _.includes(this.selected_fields, name)
                    }
                }.bind(this))
            },
            unselected_fields() {
                return _.filter(this.available_fields, {selected: false})
            }
        },
        methods: {
            toggle_field(name) {
                if (_.includes(this.selected_fields, name)) {
                    this.selected_fields.splice(this.selected_fields.indexOf(name), 1);
                }
                else {
                    if (this.single)
                        this.selected_fields.splice(0, 1);
                    this.selected_fields.push(name)
                }

            },
            select_all() {
                let fields = this.unselected_fields;
                fields.forEach((f) => this.toggle_field(f.name))
            },
            on_outside_click(e) {
                this.edit_mode = false
            }
        },
        components: {
            draggable
        }
    }
</script>
