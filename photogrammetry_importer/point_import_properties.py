import bpy

from bpy.props import (BoolProperty, EnumProperty, FloatProperty)

from photogrammetry_importer.blender_utils import add_points_as_mesh

class PointImportProperties():
    """ This class encapsulates Blender UI properties that are required to visualize the reconstructed points correctly. """
    import_points: BoolProperty(
        name="Import Points",
        description = "Import Points", 
        default=True)
    add_points_as_particle_system: BoolProperty(
        name="Add Points as Particle System",
        description="Use a particle system to represent vertex positions with objects",
        default=True)
    mesh_items = [
        ("CUBE", "Cube", "", 1),
        ("SPHERE", "Sphere", "", 2),
        ("PLANE", "Plane", "", 3)
        ]
    mesh_type: EnumProperty(
        name="Mesh Type",
        description = "Select the vertex representation mesh type.", 
        items=mesh_items)
    point_extent: FloatProperty(
        name="Initial Point Extent (in Blender Units)", 
        description = "Initial Point Extent for meshes at vertex positions",
        default=0.01)
    add_particle_color_emission: BoolProperty(
        name="Add particle color emission",
        description = "Add particle color emission to increase the visibility of the individual objects of the particle system.", 
        default=True)
        
    def import_photogrammetry_points(self, points, reconstruction_collection):
        if self.import_points:
            add_points_as_mesh(
                self, 
                points, 
                self.add_points_as_particle_system, 
                self.mesh_type, 
                self.point_extent,
                self.add_particle_color_emission,
                reconstruction_collection)