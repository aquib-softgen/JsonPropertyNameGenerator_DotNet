namespace TallySynchronizationApp.Models
{
    public class VoucherCreationDetails
    {
        public DateTime Date { get; set; }

        public DateTime? ReferenceDate { get; set; }

        public string? Reference { get; set; }

        public string VoucherType { get; set; }

        public string? VoucherTypeId { get; set; }

        public string? View { get; set; }

        public string? VoucherGSTClass { get; set; }

        public bool? IsCostCentre { get; set; }

        public string? CostCentreName { get; set; }

        public string? VoucherEntryMode { get; set; }

        public bool IsInvoice { get; set; }

        public string? VoucherNumber { get; set; }

        public bool? IsOptional { get; set; }

        public DateTime? EffectiveDate { get; set; }

        public string? Narration { get; set; }

        public string? PriceLevel { get; set; }

        //E-Invoice Details
        public string? BillToPlace { get; set; }

        public string? IRN { get; set; }

        public string? IRNAckNo { get; set; }

        public string? IRNAckDate { get; set; }

        //Dispatch Details
        public string? DeliveryNoteNo { get; set; }

        public DateTime? ShippingDate { get; set; }

        public string? DispatchFromName { get; set; }

        public string? DispatchFromStateName { get; set; }

        public string? DispatchFromPinCode { get; set; }

        public string? DispatchFromPlace { get; set; }

        //Shipping Details
        public string? DispatchDocNo { get; set; }
        public string? BasicShippedBy { get; set; }
        public string? Destination { get; set; }

        public string? CarrierName { get; set; }

        public string? BillofLandingNo { get; set; }

        public string? BillofLandingDate { get; set; }

        //Export Shipping Details
        public string? PlaceOfReceipt { get; set; }

        public string? ShipOrFlightNo { get; set; }

        public string? LandingPort { get; set; }

        public string? DischargePort { get; set; }

        public string? DesktinationCountry { get; set; }

        public string? ShippingBillNo { get; set; }

        public string? ShippingBillDate { get; set; }

        public string? PortCode { get; set; }

        //OrderDetails
        public string? BasicDueDateofPayment { get; set; }

        public string? OrderReference { get; set; }

        //Party Details
        public string? PartyName { get; set; }

        public string? PartyLedgerId { get; set; }

        public string? VoucherNumberSeries { get; set; }

        public string? PartyMailingName { get; set; }

        public string? State { get; set; }

        public string? Country { get; set; }

        public string? RegistrationType { get; set; }

        public string? PartyGSTIN { get; set; }

        public string? PlaceOfSupply { get; set; }

        public string? PINCode { get; set; }

        //Consignee Details
        public string? ConsigneeName { get; set; }

        public string? ConsigneeMailingName { get; set; }

        public string? ConsigneeState { get; set; }

        public string? ConsigneeCountry { get; set; }

        public string? ConsigneeGSTIN { get; set; }

        public string? ConsigneePinCode { get; set; }

        public bool? IsCancelled { get; set; }

        //EWAY Details
        public bool? OverrideEWayBillApplicability { get; set; }

        public string? VchType;

        public string? _MasterId;
    }
}

