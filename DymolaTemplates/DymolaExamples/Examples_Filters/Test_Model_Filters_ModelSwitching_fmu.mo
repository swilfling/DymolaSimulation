within DymolaExamples.Examples_Filters;
model Test_Model_Filters_ModelSwitching_fmu
  parameter Real y_start=0;
  parameter Real fmi_NumberOfSteps = 1000;
  parameter Real fmi_StartTime=0;
  parameter Real fmi_StopTime=10;
  Modelica.Blocks.Sources.Pulse InputSignal(
    startTime=0.1,
    period=2,
    offset=0.1)
               annotation (Placement(transformation(extent={{-84,-6},{-64,14}})));
      Chebyshev_fmu UUT(y_start=y_start,fmi_NumberOfSteps=fmi_NumberOfSteps, fmi_StartTime=fmi_StartTime,fmi_StopTime=fmi_StopTime, fmi_forceShutDownAtStopTime=true)
                                                                                                                                                                     annotation (Placement(transformation(extent={{-28,-6},
            {-8,14}})));
equation
  connect(InputSignal.y, UUT.u1)
                                annotation (Line(points={{-63,4},{-28.4,4}},
                                                              color={255,127,
          0}));
end Test_Model_Filters_ModelSwitching_fmu;
