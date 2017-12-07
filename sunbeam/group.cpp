#include <opm/parser/eclipse/EclipseState/Schedule/Group.hpp>

#include "sunbeam.hpp"


namespace {

    py::list wellnames( const Group& g, size_t timestep ) {
        return iterable_to_pylist( g.getWells( timestep )  );
    }

     int get_vfp_table( const Group& g, size_t timestep ) {
        return g.getGroupNetVFPTable(timestep);
    }
}

void sunbeam::export_Group() {

    py::class_< Group >( "Group", py::no_init )
        .add_property( "name", mkcopy( &Group::name ) )
        .def( "_vfp_table", &get_vfp_table )
        .def( "_wellnames", &wellnames )
        ;

}
