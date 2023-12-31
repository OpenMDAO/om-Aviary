"""Mass for large single aisle"""

from pyxdsm.XDSM import GROUP, XDSM
from aviary.variable_info.variables import Aircraft, Mission

x = XDSM()

x.add_system("mass", GROUP, [r"\textbf{MassSummation}"])
x.add_input("mass", [
    Aircraft.HorizontalTail.TAPER_RATIO,
    Aircraft.HorizontalTail.MOMENT_RATIO,
    Aircraft.HorizontalTail.ASPECT_RATIO,
    Aircraft.VerticalTail.MOMENT_RATIO,
    Aircraft.VerticalTail.TAPER_RATIO,
    Aircraft.Engine.REFERENCE_DIAMETER,
    Aircraft.Nacelle.CORE_DIAMETER_RATIO,
    Aircraft.Nacelle.FINENESS,
    Aircraft.Fuselage.DELTA_DIAMETER,
    Aircraft.Fuselage.NOSE_FINENESS,
    Aircraft.Fuselage.PILOT_COMPARTMENT_LENGTH,
    Aircraft.Fuselage.TAIL_FINENESS,
    Aircraft.Fuselage.WETTED_AREA_FACTOR,
    Aircraft.Wing.LOADING,
    Aircraft.Wing.THICKNESS_TO_CHORD_TIP,
    Aircraft.Design.MAX_STRUCTURAL_SPEED,
    Aircraft.Wing.ASPECT_RATIO,
    Aircraft.Wing.SWEEP,
    Mission.Design.MACH,
    Aircraft.Design.EQUIPMENT_MASS_COEFFICIENTS,
    Aircraft.Fuselage.PRESSURE_DIFFERENTIAL,
    Aircraft.Engine.SCALED_SLS_THRUST,
    Aircraft.Fuel.WING_FUEL_FRACTION,
    Aircraft.Wing.SWEEP,
    Aircraft.Wing.ASPECT_RATIO,
    Aircraft.Strut.ATTACHMENT_LOCATION_DIMENSIONLESS,
    Aircraft.CrewPayload.CARGO_MASS,
    Aircraft.Engine.MASS_SPECIFIC,
    Aircraft.Nacelle.MASS_SPECIFIC,
    Aircraft.Engine.PYLON_FACTOR,
    Aircraft.Engine.ADDITIONAL_MASS_FRACTION,
    Aircraft.Engine.MASS_SCALER,
    Aircraft.Engine.SCALE_FACTOR,
    Aircraft.Propulsion.MISC_MASS_SCALER,
    Aircraft.Engine.WING_LOCATIONS,
    Aircraft.LandingGear.MAIN_GEAR_LOCATION,
    Aircraft.VerticalTail.ASPECT_RATIO,
    Aircraft.VerticalTail.SWEEP,
    Aircraft.HorizontalTail.MASS_COEFFICIENT,
    Aircraft.LandingGear.TAIL_HOOK_MASS_SCALER,
    Aircraft.VerticalTail.MASS_COEFFICIENT,
    Aircraft.HorizontalTail.THICKNESS_TO_CHORD,
    Aircraft.HorizontalTail.VERTICAL_TAIL_FRACTION,
    Aircraft.VerticalTail.THICKNESS_TO_CHORD,
    Aircraft.Wing.HIGH_LIFT_MASS_COEFFICIENT,
    Aircraft.Wing.SURFACE_CONTROL_MASS_COEFFICIENT,
    Aircraft.Design.COCKPIT_CONTROL_MASS_COEFFICIENT,
    Aircraft.Controls.STABILITY_AUGMENTATION_SYSTEM_MASS,
    Aircraft.Controls.COCKPIT_CONTROL_MASS_SCALER,
    Aircraft.Wing.SURFACE_CONTROL_MASS_SCALER,
    Aircraft.Controls.STABILITY_AUGMENTATION_SYSTEM_MASS_SCALER,
    Aircraft.Controls.CONTROL_MASS_INCREMENT,
    Aircraft.LandingGear.MASS_COEFFICIENT,
    Aircraft.LandingGear.MAIN_GEAR_MASS_COEFFICIENT,
    Aircraft.Wing.MOUNTING_TYPE,
    Aircraft.Fuel.DENSITY,
    Aircraft.Fuel.FUEL_MARGIN,
    Aircraft.Fuel.FUEL_SYSTEM_MASS_COEFFICIENT,
    Aircraft.Fuselage.MASS_COEFFICIENT,
    "fuel_mass.fus_and_struct.pylon_len",
    "fuel_mass.fus_and_struct.MAT",
    Aircraft.Wing.MASS_SCALER,
    Aircraft.HorizontalTail.MASS_SCALER,
    Aircraft.VerticalTail.MASS_SCALER,
    Aircraft.Fuselage.MASS_SCALER,
    Aircraft.LandingGear.TOTAL_MASS_SCALER,
    Aircraft.Engine.POD_MASS_SCALER,
    Aircraft.Design.STRUCTURAL_MASS_INCREMENT,
    Aircraft.Fuel.FUEL_SYSTEM_MASS_SCALER,
    Mission.Design.GROSS_MASS,
    Aircraft.Wing.MASS_COEFFICIENT,
    Aircraft.Wing.TAPER_RATIO,
    Aircraft.Wing.THICKNESS_TO_CHORD_ROOT,
    Aircraft.HorizontalTail.VOLUME_COEFFICIENT,
    Aircraft.VerticalTail.VOLUME_COEFFICIENT,
    Aircraft.Nacelle.CLEARANCE_RATIO,
    Aircraft.Wing.FLAP_CHORD_RATIO,
    Aircraft.Wing.FLAP_SPAN_RATIO,
    Aircraft.Wing.SLAT_CHORD_RATIO,
    Aircraft.Wing.SLAT_SPAN_RATIO,
    Mission.Landing.LIFT_COEFFICIENT_MAX,
    "density",
    Aircraft.Design.EXTERNAL_SUBSYSTEMS_MASS,
])

x.add_output("mass", [
    Aircraft.HorizontalTail.AREA,
    Aircraft.HorizontalTail.SPAN,
    Aircraft.HorizontalTail.ROOT_CHORD,
    Aircraft.HorizontalTail.MOMENT_ARM,
    Aircraft.HorizontalTail.AVERAGE_CHORD,
    Aircraft.VerticalTail.AREA,
    Aircraft.VerticalTail.SPAN,
    Aircraft.VerticalTail.ROOT_CHORD,
    Aircraft.VerticalTail.MOMENT_ARM,
    Aircraft.VerticalTail.AVERAGE_CHORD,
    Aircraft.Nacelle.AVG_LENGTH,
    Aircraft.Nacelle.SURFACE_AREA,
    Aircraft.Fuselage.AVG_DIAMETER,
    "size.fuselage.cabin_height",
    "size.fuselage.cabin_len",
    "size.fuselage.nose_height",
    Aircraft.Fuselage.LENGTH,
    Aircraft.Fuselage.WETTED_AREA,
    Aircraft.TailBoom.LENGTH,
    Aircraft.Wing.AREA,
    Aircraft.Wing.SPAN,
    Aircraft.Wing.CENTER_CHORD,
    Aircraft.Wing.AVERAGE_CHORD,
    Aircraft.Wing.ROOT_CHORD,
    Aircraft.Wing.THICKNESS_TO_CHORD_UNWEIGHTED,
    Aircraft.Fuel.WING_VOLUME_STRUCTURAL_MAX,
    "max_airspeed",
    "vel_c",
    "max_maneuver_factor",
    "min_dive_vel",
    "max_mach",
    "density_ratio",
    "V9",
    Aircraft.Wing.ULTIMATE_LOAD_FACTOR,
    Aircraft.Design.FIXED_USEFUL_LOAD,
    Aircraft.Design.FIXED_EQUIPMENT_MASS,
    Aircraft.Wing.MATERIAL_FACTOR,
    "c_strut_braced",
    "c_gear_loc",
    Aircraft.Engine.POSITION_FACTOR,
    "half_sweep",
    Aircraft.CrewPayload.PASSENGER_PAYLOAD_MASS,
    "payload_mass_des",
    "payload_mass_max",
    Aircraft.Propulsion.TOTAL_ENGINE_MASS,
    Aircraft.Propulsion.TOTAL_ENGINE_POD_MASS,
    "eng_comb_mass",
    "wing_mounted_mass",
    "fixed_mass.tail.loc_MAC_vtail",
    Aircraft.HorizontalTail.MASS,
    Aircraft.VerticalTail.MASS,
    Aircraft.Wing.HIGH_LIFT_MASS,
    Aircraft.Controls.TOTAL_MASS,
    Aircraft.LandingGear.TOTAL_MASS,
    "fixed_mass.main_gear_mass",
    Aircraft.Fuel.AUXILIARY_FUEL_CAPACITY,
    "fuel_mass.body_tank.extra_fuel_volume",
    "fuel_mass.body_tank.max_extra_fuel_mass",
    "fuel_mass.wingfuel_mass_min",
    Aircraft.Fuel.TOTAL_CAPACITY,
    "fuel_mass.fuel_and_oem.OEM_wingfuel_mass",
    "fuel_mass.fuel_and_oem.OEM_fuel_vol",
    Aircraft.Fuel.WING_VOLUME_DESIGN,
    Aircraft.Design.OPERATING_MASS,
    "fuel_mass.fuel_and_oem.payload_mass_max_fuel",
    "fuel_mass.fuel_and_oem.volume_wingfuel_mass",
    "fuel_mass.max_wingfuel_mass",
    Aircraft.Fuel.WING_VOLUME_STRUCTURAL_MAX,
    "fuel_mass.fus_mass_full",
    Aircraft.Fuel.FUEL_SYSTEM_MASS,
    Aircraft.Design.STRUCTURE_MASS,
    Aircraft.Fuselage.MASS,
    Mission.Design.FUEL_MASS,
    Aircraft.Propulsion.MASS,
    Mission.Design.FUEL_MASS_REQUIRED,
    "fuel_mass.fuel_mass_min",
    "wing_mass.isolated_wing_mass",
    Aircraft.Wing.MASS,
    Aircraft.Nacelle.AVG_DIAMETER,
], side="right")

x.write("mass_large_single_aisle_1_xdsm")
x.write_sys_specs("mass_large_single_aisle_1_specs")
