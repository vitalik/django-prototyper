<template>
    <div class="card card-body">

        <div class="row">
            <div class="col-md-3">
                {{ attribute }}
            </div>
            <div class="col-md-6" v-click-outside="on_outside_click">

                <draggable v-model="selected_fields" element="span">
                    <div class="row">
                        <div v-for="fld in selected_fields">
                            <a @click="toggle_order(fld)"
                               class="btn btn-sm"
                               href="javascript:void(0)">
                                {{ fld.reverse ? '-' : '+' }}
                            </a>
                            <a @click="toggle_field(fld)"
                               class="badge badge-secondary mr-1"
                               href="javascript:void(0)">
                                {{ fld.name }}
                            </a>
                            <span>|</span>
                        </div>
                    </div>
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
                            <a @click="toggle_field(fld)"
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
        name: 'SelectNegativeFields',
        props: ['model', 'attribute', 'single'],
        data() {
            return {
                selected_fields: [],
                edit_mode: false,
            }
        },
        computed: {
            applicable_fields() {
                // TODO: based on attribute
                return _.map(this.model.fields, 'name')
            },
            available_fields() {
                return _.map(this.applicable_fields, function (name) {
                    const field = _.find(this.selected_fields, {name});
                    return {
                        name,
                        'reverse': field ? field.reverse : false,
                        'selected': !!field,
                    }
                }.bind(this))
            },
            unselected_fields() {
                return _.filter(this.available_fields, {selected: false})
            }
        },
        methods: {
            toggle_field(field) {
                if (_.includes(_.map(this.selected_fields, 'name'), field.name))
                    this.selected_fields = _.filter(this.selected_fields, i => (i.name != field.name));
                else {
                    if (this.single)
                        this.selected_fields = [];
                    this.selected_fields.push(field);
                }
            },
            toggle_order(field) {
                const index = _.findIndex(this.selected_fields, {'name': field.name});
                if (index === -1) return;
                let selected_field = this.selected_fields[index];
                selected_field.reverse = !selected_field.reverse;
                if (selected_field) {
                    this.$set(this.selected_fields, index, selected_field)
                }
            },
            select_all() {
                let fields = this.unselected_fields;
                fields.forEach((f) => this.toggle_field(f))
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
