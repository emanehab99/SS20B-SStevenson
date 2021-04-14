"""
Mapping model field names and values
"""
MASS_1_LABEL = 'MASS 1'
MASS_2_LABEL = 'MASS 2'
METALICITY_LABEL = 'Metallicity'
ECCENTRICITY_LABEL = 'Eccentricity'
ORBITAL_PERIOD_LABEL = 'Period'
SEPARATION_LABEL = 'Separation'
MAX_TIME_LABEL = 'Maximum Time'

VELOCITY_RANDOM_NUMBER_1_LABEL = 'Velocity Random Number 1'
VELOCITY_1_LABEL = 'Velocity 1'
THETA_1_LABEL = 'Theta 1'
PHI_1_LABEL = 'Phi 1'
MEAN_ANOMALY_1_LABEL = 'Mean Anomaly 1'

VELOCITY_RANDOM_NUMBER_2_LABEL = 'Velocity Random Number 2'
VELOCITY_2_LABEL = 'Velocity 2'
THETA_2_LABEL = 'Theta 2'
PHI_2_LABEL = 'Phi 2'
MEAN_ANOMALY_2_LABEL = 'Mean Anomaly 2'

##########################
# COMMON ENVELOPE
##########################
COMMON_ENVELOPE_ALPHA_LABEL = 'common_envelope_alpha'
COMMON_ENVELOPE_LAMBDA_PRESCRIPTION = 'common_envelope_lambda_prescription'
COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_FIXED = 'LAMBDA_FIXED'
COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_FIXED_VALUE = 'LAMBDA_FIXED'
COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_LOVERIDGE = 'LAMBDA_LOVERIDGE'
COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_LOVERIDGE_VALUE = 'LAMBDA_LOVERIDGE'
COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_NANJING = 'LAMBDA_NANJING'
COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_NANJING_VALUE = 'LAMBDA_NANJING'
COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_KRUCKOW = 'LAMBDA_KRUCKOW'
COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_KRUCKOW_VALUE = 'LAMBDA_KRUCKOW'
COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_DEWI = 'LAMBDA_DEWI'
COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_DEWI_VALUE = 'LAMBDA_DEWI'
COMMON_ENVELOPE_LAMBDA_LABEL = 'common_envelope_lambda'


COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_CHOICES = [
    (COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_FIXED_VALUE, COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_FIXED),
    (COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_KRUCKOW_VALUE, COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_KRUCKOW),
    (COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_LOVERIDGE_VALUE, COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_LOVERIDGE),
    (COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_NANJING_VALUE, COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_NANJING),
    (COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_DEWI_VALUE, COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_DEWI),
]
##########################
# Supernova
##########################
REMNANT_MASS_PRESCRIPTION_LABEL = 'remnant_mass_prescription'
REMNANT_MASS_PRESCRIPTION_HURLEY2000 = 'HURLEY2000'
REMNANT_MASS_PRESCRIPTION_HURLEY2000_VALUE = 'HURLEY2000'
REMNANT_MASS_PRESCRIPTION_BELCZYNSKI2002 = 'BELCZYNSKI2002'
REMNANT_MASS_PRESCRIPTION_BELCZYNSKI2002_VALUE = 'BELCZYNSKI2002'
REMNANT_MASS_PRESCRIPTION_FRYER2012 = 'FRYER2012'
REMNANT_MASS_PRESCRIPTION_FRYER2012_VALUE = 'FRYER2012'
REMNANT_MASS_PRESCRIPTION_MULLER2016 = 'MULLER2016'
REMNANT_MASS_PRESCRIPTION_MULLER2016_VALUE = 'MULLER2016'
REMNANT_MASS_PRESCRIPTION_MULLERMANDEL = 'MULLERMANDEL'
REMNANT_MASS_PRESCRIPTION_MULLERMANDEL_VALUE = 'MULLERMANDEL'

REMNANT_MASS_PRESCRIPTION_CHOICES = [
    (REMNANT_MASS_PRESCRIPTION_HURLEY2000_VALUE, REMNANT_MASS_PRESCRIPTION_HURLEY2000),
    (REMNANT_MASS_PRESCRIPTION_BELCZYNSKI2002_VALUE, REMNANT_MASS_PRESCRIPTION_BELCZYNSKI2002),
    (REMNANT_MASS_PRESCRIPTION_FRYER2012_VALUE, REMNANT_MASS_PRESCRIPTION_FRYER2012),
    (REMNANT_MASS_PRESCRIPTION_MULLER2016_VALUE, REMNANT_MASS_PRESCRIPTION_MULLER2016),
    (REMNANT_MASS_PRESCRIPTION_MULLERMANDEL_VALUE, REMNANT_MASS_PRESCRIPTION_MULLERMANDEL),
]

FRYER_SUPERNOVA_ENGINE_LABEL = 'fryer_supernova_engine'
FRYER_SUPERNOVA_ENGINE_DELAYED = 'DELAYED'
FRYER_SUPERNOVA_ENGINE_DELAYED_VALUE = 'DELAYED'
FRYER_SUPERNOVA_ENGINE_RAPID = 'RAPID'
FRYER_SUPERNOVA_ENGINE_RAPID_VALUE = 'RAPID'

FRYER_SUPERNOVA_ENGINE_CHOICES = [
    (FRYER_SUPERNOVA_ENGINE_DELAYED_VALUE, FRYER_SUPERNOVA_ENGINE_DELAYED),
    (FRYER_SUPERNOVA_ENGINE_RAPID_VALUE, FRYER_SUPERNOVA_ENGINE_RAPID),
]

BLACK_HOLE_KICKS_LABEL = 'black_hole_kicks'
BLACK_HOLE_KICKS_FULL = 'FULL'
BLACK_HOLE_KICKS_FULL_VALUE = 'FULL'
BLACK_HOLE_KICKS_REDUCED = 'REDUCED'
BLACK_HOLE_KICKS_REDUCED_VALUE = 'REDUCED'
BLACK_HOLE_KICKS_ZERO = 'ZERO'
BLACK_HOLE_KICKS_ZERO_VALUE = 'ZERO'
BLACK_HOLE_KICKS_FALLBACK = 'FALLBACK'
BLACK_HOLE_KICKS_FALLBACK_VALUE = 'FALLBACK'

BLACK_HOLE_KICKS_CHOICES = [
    (BLACK_HOLE_KICKS_FALLBACK_VALUE, BLACK_HOLE_KICKS_FALLBACK),
    (BLACK_HOLE_KICKS_FULL_VALUE, BLACK_HOLE_KICKS_FULL),
    (BLACK_HOLE_KICKS_REDUCED_VALUE, BLACK_HOLE_KICKS_REDUCED),
    (BLACK_HOLE_KICKS_ZERO_VALUE, BLACK_HOLE_KICKS_ZERO_VALUE),
]

# ZERO, FIXED, FLAT, MAXWELLIAN, BRAYELDRIDGE, MULLER2016, MULLER2016MAXWELLIAN, MULLERMANDEL

KICK_VELOCITY_DISTRIBUTION = 'kick-magnitude-distribution'
KICK_VELOCITY_DISTRIBUTION_LABEL = 'kick_velocity_distribution'
KICK_VELOCITY_DISTRIBUTION_ZERO = 'ZERO'
KICK_VELOCITY_DISTRIBUTION_ZERO_VALUE = 'ZERO'
KICK_VELOCITY_DISTRIBUTION_FIXED = 'FIXED'
KICK_VELOCITY_DISTRIBUTION_FIXED_VALUE = 'FIXED'
KICK_VELOCITY_DISTRIBUTION_FLAT = 'FLAT'
KICK_VELOCITY_DISTRIBUTION_FLAT_VALUE = 'FLAT'
KICK_VELOCITY_DISTRIBUTION_MAXWELLIAN = 'MAXWELLIAN'
KICK_VELOCITY_DISTRIBUTION_MAXWELLIAN_VALUE = 'MAXWELLIAN'
KICK_VELOCITY_DISTRIBUTION_BRAYELDRIDGE = 'BRAYELDRIDGE'
KICK_VELOCITY_DISTRIBUTION_BRAYELDRIDGE_VALUE = 'BRAYELDRIDGE'
KICK_VELOCITY_DISTRIBUTION_MULLER2016 = 'MULLER2016'
KICK_VELOCITY_DISTRIBUTION_MULLER2016_VALUE = 'MULLER2016'
KICK_VELOCITY_DISTRIBUTION_MULLER2016MAXWELLIAN = 'MULLER2016MAXWELLIAN'
KICK_VELOCITY_DISTRIBUTION_MULLER2016MAXWELLIAN_VALUE = 'MULLER2016MAXWELLIAN'
KICK_VELOCITY_DISTRIBUTION_MULLERMANDEL = 'MULLERMANDEL'
KICK_VELOCITY_DISTRIBUTION_MULLERMANDEL_VALUE = 'MULLERMANDEL'


KICK_VELOCITY_DISTRIBUTION_CHOICES = [
    (KICK_VELOCITY_DISTRIBUTION_ZERO_VALUE, KICK_VELOCITY_DISTRIBUTION_ZERO),
    (KICK_VELOCITY_DISTRIBUTION_FIXED_VALUE, KICK_VELOCITY_DISTRIBUTION_FIXED),
    (KICK_VELOCITY_DISTRIBUTION_FLAT_VALUE, KICK_VELOCITY_DISTRIBUTION_FLAT),
    (KICK_VELOCITY_DISTRIBUTION_MAXWELLIAN_VALUE, KICK_VELOCITY_DISTRIBUTION_MAXWELLIAN),
    (KICK_VELOCITY_DISTRIBUTION_BRAYELDRIDGE_VALUE, KICK_VELOCITY_DISTRIBUTION_BRAYELDRIDGE),
    (KICK_VELOCITY_DISTRIBUTION_MULLER2016_VALUE, KICK_VELOCITY_DISTRIBUTION_MULLER2016),
    (KICK_VELOCITY_DISTRIBUTION_MULLER2016MAXWELLIAN_VALUE, KICK_VELOCITY_DISTRIBUTION_MULLER2016MAXWELLIAN),
    (KICK_VELOCITY_DISTRIBUTION_MULLERMANDEL_VALUE, KICK_VELOCITY_DISTRIBUTION_MULLERMANDEL),
]

KICK_VELOCITY_SIGMA_CCSN_NS_LABEL = 'kick_velocity_sigma_CCSN_NS'
KICK_VELOCITY_SIGMA_CCSN_BH_LABEL = 'kick_velocity_sigma_CCSN_BH'
KICK_VELOCITY_SIGMA_ECSN_LABEL = 'kick_velocity_sigma_ECSN'
KICK_VELOCITY_SIGMA_USSN_LABEL = 'kick_velocity_sigma_USSN'

PAIR_INSTABILITY_SUPERNOVAE_LABEL = 'Pair Instability Supernovae'
PISN_LOWER_LIMIT_LABEL = 'PISN_lower_limit'
PISN_UPPER_LIMIT_LABEL = 'PISN_upper_limit'

PULSATIONAL_PAIR_INSTABILITY_SUPERNOVAE_LABEL = 'Pair Instability Supernovae'
PPI_LOWER_LIMIT_LABEL = 'PPI_lower_limit'
PPI_UPPER_LIMIT_LABEL = 'PPI_upper_limit'

PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_LABEL = 'pulsational_pair_instability_prescription'
PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_COMPAS = 'COMPAS'
PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_COMPAS_VALUE = 'COMPAS'
PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_STARTRACK = 'STARTRACK'
PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_STARTRACK_VALUE = 'STARTRACK'
PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_MARCHANT = 'MARCHANT'
PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_MARCHANT_VALUE = 'MARCHANT'

PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_CHOICES = [
    (PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_COMPAS_VALUE, PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_COMPAS),
    (PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_STARTRACK_VALUE, PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_STARTRACK),
    (PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_MARCHANT_VALUE, PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_MARCHANT),
]

MAXIMUM_NEUTRON_STAR_MASS_LABEL = 'maximum_neutron_star_mass'

##########################
# Mass Transfer
##########################
MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_LABEL = 'mass-transfer-angular-momentum-loss-prescription'
MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_JEANS = 'JEANS'
MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_JEANS_VALUE = 'JEANS'
MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ISOTROPIC = 'ISOTROPIC'
MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ISOTROPIC_VALUE = 'ISOTROPIC'
MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_CIRCUMBINARY = 'CIRCUMBINARY'
MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_CIRCUMBINARY_VALUE = 'CIRCUMBINARY'
MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ARBITRARY = 'ARBITRARY'
MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ARBITRARY_VALUE = 'ARBITRARY'

MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_CHOICES = [
    (
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ARBITRARY_VALUE,
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ARBITRARY,
    ),
    (
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ISOTROPIC_VALUE,
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ISOTROPIC,
    ),
    (
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_JEANS_VALUE,
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_JEANS,
    ),
    (
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_CIRCUMBINARY_VALUE,
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_CIRCUMBINARY,
    ),
]

MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_LABEL = 'mass-transfer-accertion-efficieny-prescription'
MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_THERMAL = 'THERMAL'
MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_THERMAL_VALUE = 'THERMAL'
MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_FIXED = 'FIXED'
MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_FIXED_VALUE = 'FIXED'


MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_CHOICES = [
    (
        MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_THERMAL_VALUE,
        MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_THERMAL,
    ),
    (
        MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_FIXED_VALUE,
        MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_FIXED,
    ),
]

MASS_TRANSFER_FA_LABEL = 'mass_transfer_fa'
MASS_TRANSFER_JLOSS_LABEL = 'mass_transfer_jloss'

NAME_VALUES = dict()


NAME_VALUES.update(
    {
        COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_FIXED: COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_FIXED_VALUE,
        COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_KRUCKOW: COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_KRUCKOW_VALUE,
        COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_LOVERIDGE: COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_LOVERIDGE_VALUE,
        COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_NANJING: COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_NANJING_VALUE,
        COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_DEWI: COMMON_ENVELOPE_LAMBDA_PRESCRIPTION_DEWI_VALUE,
        REMNANT_MASS_PRESCRIPTION_HURLEY2000: REMNANT_MASS_PRESCRIPTION_HURLEY2000_VALUE,
        REMNANT_MASS_PRESCRIPTION_BELCZYNSKI2002: REMNANT_MASS_PRESCRIPTION_BELCZYNSKI2002_VALUE,
        REMNANT_MASS_PRESCRIPTION_FRYER2012: REMNANT_MASS_PRESCRIPTION_FRYER2012_VALUE,
        REMNANT_MASS_PRESCRIPTION_MULLER2016: REMNANT_MASS_PRESCRIPTION_MULLER2016_VALUE,
        REMNANT_MASS_PRESCRIPTION_MULLERMANDEL: REMNANT_MASS_PRESCRIPTION_MULLERMANDEL_VALUE,
        FRYER_SUPERNOVA_ENGINE_DELAYED: FRYER_SUPERNOVA_ENGINE_DELAYED_VALUE,
        FRYER_SUPERNOVA_ENGINE_RAPID: FRYER_SUPERNOVA_ENGINE_RAPID_VALUE,
        BLACK_HOLE_KICKS_FALLBACK: BLACK_HOLE_KICKS_FALLBACK_VALUE,
        BLACK_HOLE_KICKS_FULL: BLACK_HOLE_KICKS_FULL_VALUE,
        BLACK_HOLE_KICKS_REDUCED: BLACK_HOLE_KICKS_REDUCED_VALUE,
        BLACK_HOLE_KICKS_ZERO: BLACK_HOLE_KICKS_ZERO_VALUE,
        KICK_VELOCITY_DISTRIBUTION_ZERO: KICK_VELOCITY_DISTRIBUTION_ZERO_VALUE,
        KICK_VELOCITY_DISTRIBUTION_FIXED: KICK_VELOCITY_DISTRIBUTION_FIXED_VALUE,
        KICK_VELOCITY_DISTRIBUTION_FLAT: KICK_VELOCITY_DISTRIBUTION_FLAT_VALUE,
        KICK_VELOCITY_DISTRIBUTION_MAXWELLIAN: KICK_VELOCITY_DISTRIBUTION_MAXWELLIAN_VALUE,
        KICK_VELOCITY_DISTRIBUTION_BRAYELDRIDGE: KICK_VELOCITY_DISTRIBUTION_BRAYELDRIDGE_VALUE,
        KICK_VELOCITY_DISTRIBUTION_MULLER2016: KICK_VELOCITY_DISTRIBUTION_MULLER2016_VALUE,
        KICK_VELOCITY_DISTRIBUTION_MULLER2016MAXWELLIAN: KICK_VELOCITY_DISTRIBUTION_MULLER2016MAXWELLIAN_VALUE,
        KICK_VELOCITY_DISTRIBUTION_MULLERMANDEL: KICK_VELOCITY_DISTRIBUTION_MULLERMANDEL_VALUE,
        PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_COMPAS: PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_COMPAS_VALUE,
        PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_STARTRACK: PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_STARTRACK_VALUE,
        PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_MARCHANT: PULSATIONAL_PAIR_INSTABILITY_PRESCRIPTION_MARCHANT_VALUE,
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ARBITRARY: MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ARBITRARY_VALUE,
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ISOTROPIC: MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_ISOTROPIC_VALUE,
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_JEANS: MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_JEANS_VALUE,
        MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_CIRCUMBINARY: MASS_TRANSFER_ANGULAR_MOMENTUM_LOSS_PRESCRIPTION_CIRCUMBINARY_VALUE,
        MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_THERMAL: MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_THERMAL_VALUE,
        MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_FIXED: MASS_TRANSFER_ACCERTION_EFFICIENCY_PRESCRIPTION_FIXED_VALUE,
    }
)

## Mapping fields names to corresponding COMPAS commands
FIELD_COMMANDS = dict(
    {
        'mass1': '--initial-mass-1',
        'mass2': '--initial-mass-2',
        'metallicity': '--metallicity',
        'eccentricity': '--eccentricity',
        'separation': '--semi-major-axis',
        'orbital_period': '--orbital-period',
        'max_time': '--maximum-evolution-time',
        'velocity_random_number_1': '--kick-magnitude-random-1',
        'velocity_random_number_2': '--kick-magnitude-random-2',
        'velocity_1': '--kick-magnitude-1',
        'velocity_2': '--kick-magnitude-2',
        'theta_1': '--kick-theta-1',
        'theta_2': '--kick-theta-2',
        'phi_1': '--kick-phi-1',
        'phi_2': '--kick-phi-2',
        'mean_anomaly_1': '--kick-mean-anomaly-1',
        'mean_anomaly_2': '--kick-mean-anomaly-2',
        'common_envelope_alpha': '--common-envelope-alpha',
        'common_envelope_lambda_prescription': '--common-envelope-lambda-prescription',
        'common_envelope_lambda': '--common-envelope-lambda',
        'remnant_mass_prescription': '--remnant-mass-prescription',
        'fryer_supernova_engine': '--fryer-supernova-engine',
        'black_hole_kicks': '--black-hole-kicks',
        'Kick_velocity_distribution': '--kick-magnitude-distribution',
        'kick_velocity_sigma_CCSN_NS': '--kick-magnitude-sigma-CCSN-NS',
        'kick_velocity_sigma_CCSN_BH': '--kick-magnitude-sigma-CCSN-BH',
        'kick_velocity_sigma_ECSN': '--kick-magnitude-sigma-ECSN',
        'kick_velocity_sigma_USSN': '--kick-magnitude-sigma-USSN',
        'pair_instability_supernovae': '--pair-instability-supernovae',
        'pisn_lower_limit': '--pisn-lower-limit',
        'pisn_upper_limit': '--pisn-upper-limit',
        'pulsational_pair_instability_supernovae': '--pulsational-pair-instability',
        'ppi_lower_limit': '--ppi-lower-limit',
        'ppi_upper_limit': '--ppi-upper-limit',
        'pulsational_pair_instability_prescription': '--pulsational-pair-instability-prescription',
        'maximum_neutron_star_mass': '--maximum-neutron-star-mass',
        'mass_transfer_angular_momentum_loss_prescription': '--mass-transfer-angular-momentum-loss-prescription',
        'mass_transfer_accertion_efficiency_prescription': '--mass-transfer-accretion-efficiency-prescription',
        'mass_transfer_fa': '--mass-transfer-fa',
        'mass_transfer_jloss': '--mass-transfer-jloss',
    }
)

INITIAL_PARAMETERS = [
    'mass1',
    'mass2',
    'metallicity',
    'eccentricity',
    'separation',
    'orbital_period',
    'max_time',
]

ADVANCED_SETTINGS = [
    'velocity_random_number_1',
    'velocity_1',
    'theta_1',
    'phi_1',
    'mean_anomaly_1',
    'velocity_random_number_2',
    'velocity_2',
    'theta_2',
    'phi_2',
    'mean_anomaly_2',
    'common_envelope_alpha',
    'common_envelope_lambda_prescription',
    'common_envelope_lambda',
    'remnant_mass_prescription',
    'fryer_supernova_engine',
    'black_hole_kicks',
    'Kick_velocity_distribution',
    'kick_velocity_sigma_CCSN_NS',
    'kick_velocity_sigma_CCSN_BH',
    'kick_velocity_sigma_ECSN',
    'kick_velocity_sigma_USSN',
    'pair_instability_supernovae',
    'pisn_lower_limit',
    'pisn_upper_limit',
    'pulsational_pair_instability_supernovae',
    'ppi_lower_limit',
    'ppi_upper_limit',
    'pulsational_pair_instability_prescription',
    'maximum_neutron_star_mass',
    'mass_transfer_angular_momentum_loss_prescription',
    'mass_transfer_accertion_efficiency_prescription',
    'mass_transfer_fa',
    'mass_transfer_jloss',
    'kick_enabled',
    'common_envelope_enabled',
    'mass_transfer_enabled',
    'supernova_enabled',
]

KICK_SETTINGS = [
    'velocity_random_number_1',
    'velocity_1',
    'theta_1',
    'phi_1',
    'mean_anomaly_1',
    'velocity_random_number_2',
    'velocity_2',
    'theta_2',
    'phi_2',
    'mean_anomaly_2',
]

COMMON_ENVELOPE_SETTINGS = [
    'common_envelope_alpha',
    'common_envelope_lambda_prescription',
    'common_envelope_lambda',
]

SUPERNOVA_SETTINGS = [
    'remnant_mass_prescription',
    'fryer_supernova_engine',
    'black_hole_kicks',
    'Kick_velocity_distribution',
    'kick_velocity_sigma_CCSN_NS',
    'kick_velocity_sigma_CCSN_BH',
    'kick_velocity_sigma_ECSN',
    'kick_velocity_sigma_USSN',
    'pair_instability_supernovae',
    'pisn_lower_limit',
    'pisn_upper_limit',
    'pulsational_pair_instability_supernovae',
    'ppi_lower_limit',
    'ppi_upper_limit',
    'pulsational_pair_instability_prescription',
    'maximum_neutron_star_mass',
]

MASS_TRANSFER_SETTINGS = [
    'mass_transfer_angular_momentum_loss_prescription',
    'mass_transfer_accertion_efficiency_prescription',
    'mass_transfer_fa',
    'mass_transfer_jloss',
]

########################
# CELERY TASK Results
########################
TASK_SUCCESS = 'SUCCESS'
TASK_FAIL = 'FAIL'
TASK_TIMEOUT = 'TIMEOUT'
TASK_RUNNING = 'RUNNING'
# example of added task failure
TASK_FAIL_OTHER = 'REMOVED'
